"""
====================================================================================
File                :   tags_master.py
Description         :   This file contains code related to the Tags master API.
Author              :   Haritha sree S
Date Created        :   May 12th 2024
Last Modified BY    :   Haritha sree S
Date Modified       :   May 12th 2024
====================================================================================
"""
 
from django.conf import settings
from db_interface.queries import *
from db_interface.execute import *
from django.views.decorators.csrf import csrf_exempt
from utilities.constants import *
from datetime import datetime
from a2z_ecom.globals import *
from a2z_ecom.functionlity import *
 
import json,uuid,math
 
 
@csrf_exempt
@require_methods(["POST","PUT","DELETE"])
@validate_access_token
@handle_exceptions
def tags_master(request):
    """
    Inserts datas into the master.
 
    Args:
        request (HttpRequest): The HTTP request object containing the data to be inserted.
 
    Returns:
        JsonResponse: A JSON response indicating the result of the data insertion.
 
    The `tags_master` API is responsible for adding new records to the master database.
    It expects an HTTP request object containing the data to be inserted. The data should be in a
    specific format, such as JSON, and must include the necessary fields required by the master database.
    """
    data = json.loads(request.body)
    utc_time = datetime.utcnow()  
    user_id = request.user[0]["ref_user_id"]
    user_type = request.user[0]["user_type"]
    table_name = "tags_master"
 
    #To create the data
    if request.method == "POST":
        #To throw an required error message
        errors = {
            'tag_name': {'req_msg': 'Tag name is required','val_msg': '', 'type': ''}  
        }
        validation_errors = validate_data(data,errors)
        if validation_errors:
            return JsonResponse({'status': 400, 'action': 'error', 'message': validation_errors, "message_type":"specific"}, safe=False)
       
        tag_name = data["tag_name"]  
        uniq_name = format_string_to_slug(tag_name)
        duplicate_check = check_unique_name(table_name, "uniq_name", uniq_name, "tag_name")
        if duplicate_check:
            return duplicate_check
       
        query = """
            INSERT INTO tags_master
            (tag_name, created_date, modified_date, created_by, modified_by, uniq_name)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING data_uniq_id;
        """
        params = (
            tag_name,
            utc_time,      
            utc_time,      
            user_id,        
            user_id,      
            uniq_name
        )
       
        success_message = "Data created successfully"
        error_message = "Failed to create data"
   
    #To modify the data
    elif request.method == "PUT":
        #To throw an required error message
        errors = {
            'tag_name': {'req_msg': 'Tag name is required','val_msg': '', 'type': ''} ,
            'data_uniq_id': {'req_msg': 'Tag ID is required','val_msg': '', 'type': ''}  
        }
        validation_errors = validate_data(data,errors)
        if validation_errors:
             return JsonResponse({'status': 400, 'action': 'error', 'message': validation_errors, "message_type":"specific"}, safe=False)
       
        data_uniq_id = base64_operation(data["data_uniq_id"],'decode')  
        tag_name = data["tag_name"]  
 
        uniq_name = format_string_to_slug(tag_name)
        duplicate_check = check_unique_name(table_name, "uniq_name", uniq_name, "tag_name", data_uniq_id)
        if duplicate_check:
            return duplicate_check
 
        query = """
            UPDATE tags_master
            SET tag_name   = %s,
                modified_date = %s,
                modified_by   = %s,
                uniq_name     = %s
            WHERE data_uniq_id = %s
            RETURNING data_uniq_id;
        """
        params = (
            tag_name,
            utc_time,
            user_id,
            uniq_name,
            data_uniq_id
        )
       
        success_message = "Data updated successfully"
        error_message = "Failed to update data"            
   
    #To delete the data
    elif request.method == "DELETE":
        errors = {
            'data_uniq_id': {'req_msg': 'Tag ID is required','val_msg': '', 'type': ''}  
        }
        validation_errors = validate_data(data,errors)
        if validation_errors:
             return JsonResponse({'status': 400, 'action': 'error', 'message': validation_errors, "message_type":"specific"}, safe=False)
       
        data_uniq_id = base64_operation(data["data_uniq_id"],'decode')  
        query = """
            DELETE FROM tags_master
            WHERE data_uniq_id = %s RETURNING data_uniq_id;
        """
        params = (data_uniq_id,)
        success_message = "Data deleted successfully"
        error_message = "Failed to delete data"
   
    execute = execute_query(query,params)
    data_uniq_id = execute[0]["data_uniq_id"]
   
    if execute!=0:
        message = {
                'action':'success',
                'message':success_message,
                'data_uniq_id':base64_operation(data_uniq_id, 'encode')
                }
        return JsonResponse(message, safe=False,status = 200)                    
    else:
        message = {                        
                'action':'error',
                'message': error_message
                }
        return JsonResponse(message, safe=False, status = 400)  
       
 
@csrf_exempt
@require_methods(["GET"])
@validate_access_token
@handle_exceptions
def tags_master_get(request):
 
    """
    Retrieves data from the master database.
 
    Args:
        request (HttpRequest): The HTTP request object containing parameters for data retrieval.
 
    Returns:
        JsonResponse: A JSON response indicating the result of the data retrieval.
 
    The `tags_master_get` API is responsible for fetching data from the master database
    based on the parameters provided in the HTTP request. The request may include filters, sorting
    criteria, or other parameters to customize the query.
    """
   
    utc_time = datetime.utcnow()
    table_name = 'tags_master'
    user_type = request.user[0]["user_type"]
    user_id = request.user[0]["ref_user_id"]
 
    search_input = request.GET.get('search_input',None)
   
    #To filter using limit,from_date,to_date,active_status,order_type,order_field
    limit_offset,search_join,items_per_page,page_number,order_by = data_filter(request,table_name)
 
    if search_input:
        search_join = search_filter_get(search_input,table_name,user_id,search_join)
 
    if search_input:
        search_input = search_input.strip()
        search_join += " AND  {table_name}.tag_name ILIKE '%{inp}%' ".format(inp=search_input,table_name=table_name)
 
    #Query to make the count of data
    count_query = """ SELECT count(*) as count
    FROM {table_name}
    WHERE 1=1 {search_join};""".format(search_join=search_join,table_name=table_name)
    get_count = search_all(count_query)
 
    #Query to fetch all the data
    fetch_data_query = """ SELECT *, TO_CHAR({table_name}.created_date, 'Mon DD, YYYY | HH12:MI AM') as created_f_date,
    (select first_name from user_master where user_master.data_uniq_id = tags_master.created_by) as created_user FROM tags_master
    WHERE 1=1  {search_join} {order_by} {limit};""".format(search_join=search_join,order_by=order_by,limit=limit_offset,table_name=table_name)
                       
    get_all_data = search_all(fetch_data_query)
   
    if len(get_count)!=0:                        
        count = get_count[0]['count']
        total_pages = math.ceil(count / items_per_page)
    else:
        message = {
                'action':'error',
                'message': "Failed to make the count"
                }
        return JsonResponse(message, safe=False,status = 400)
   
    for index,i in enumerate(get_all_data):
        i['data_uniq_id'] = base64_operation(i['data_uniq_id'],'encode')
        i['created_by'] = base64_operation(i['created_by'],'encode')
 
        #To get encoded data_uniq_id,serial number,formatted,readable created and modified_date
        data_format(data=i,page_number=page_number,index=index)
                           
    message = {
            'action':'success',
            'data':get_all_data,  
            'page_number': page_number,
            'items_per_page': items_per_page,
            'total_pages': total_pages,
            'total_items': count,
            'table_name':table_name                                                        
 
            }
    return JsonResponse(message,safe=False,status = 200)