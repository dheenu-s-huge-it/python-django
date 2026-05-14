from django.urls import path
from product_app.brand_master import *
from product_app.stock_master import *
from product_app.weight_master import *
from product_app.product import *
from product_app.length_master import *
from product_app.product_get import *
from product_app.product_updates import *
from product_app.product_edit import *
from product_app.product_web import *
from product_app.option_master import *
from product_app.review import *
from product_app.ledger import *
from product_app.tag_master import *
from product_app.logo_master import *
from product_app.payout_master import *
 
 
urlpatterns = [
    # BRAND MASTER START /////
    path('brand/create',brand_master,name='brand_master'),
    path('brand/get',brand_master_get,name='brand_master_get'),
    path('brand/status/change',brand_master_status, name='brand_master_status'),
    # BRAND MASTER END ///////
   
    # OPTION MASTER START /////
    path('option/master/create',option_master_create,name='option_master_create'),
    path('option/master/edit',option_master_edit,name='option_master_edit'),
    path('option/master/get',option_master_table_get,name='option_master_table_get'),
    # OPTION MASTER END ///////  
 
    # STOCK MASTER START /////
    path('stock/create',stock_master,name='stock_master'),
    path('stock/get',stock_master_get,name='stock_master_get'),
    # STOCK MASTER END ///////    
 
    # WEIGHT MASTER START /////
    path('weight/create',weight_master,name='weight_master'),
    path('weight/get',weight_master_get,name='weight_master_get'),
    # WEIGHT MASTER END ///////
 
    # LENGTH MASTER START /////
    path('length/create',length_master,name='length_master'),
    path('length/get',length_master_get,name='length_master_get'),
    # LENGTH MASTER END ///////
 
    # PRODUCT MASTER CREATE RELATED APIS START /////
    path('create',product_create,name='product_create'),
    path('specs/create',product_spec_create,name='product_spec_create'),
    path('options/create',product_options_create,name='product_options_create'),
    path('options/config/create',product_option_config,name='product_option_config'),
    path('update/stock',update_stock,name='update_stock'),
    path('update/approval',product_approval,name='product_approval'),
    path('feature/status/change',product_feature_status_change,name='product_feature_status_change'),
    path('delete',product_delete,name='product_delete'),
    # PRODUCT MASTER CREATE RELATED APIS END ///////
 
    # PRODUCT MASTER GET RELATED APIS START /////
    path('get',product_master_get,name='product_master_get'),
    path('variant/get',prod_option_variant_get,name='prod_option_variant_get'), #not used api
    path('sep/option/variant/get',prod_variant_get,name='prod_variant_get'),
    path('specs/get',product_specifications_get,name='product_specifications_get'),
    path('option/config/get',product_config_get,name='product_config_get'),
    path('variant/skucode/get',get_variant_sku_code,name='get_variant_sku_code'),
    path('history/get',product_history_get,name='product_history_get'),
    path('variant/create',product_variants_create,name='product_variants_create'),
    # PRODUCT MASTER GET RELATED APIS START /////
 
    # PRODUCT MASTER EDIT RELATED APIS START /////
    path('edit',product_edit_new,name='product_edit'),
    path('specs/edit',product_spec_edit,name='product_spec_edit'),
    path('variant/edit',product_variants_edit,name='product_variants_edit'),
    path('options/config/edit',product_option_config_edit,name='product_option_config_edit'),
    # PRODUCT MASTER EDIT RELATED APIS START /////
 
    # PRODUCT MASTER APPROVED EDIT RELATED APIS START /////
    path('approved/edit',product_edit_new,name='product_edit'),
    path('approved/specs/edit',product_spec_edit,name='product_spec_edit'),
    path('approved/option/edit',product_options_edit,name='product_options_edit'),
    path('approved/variant/edit',product_variants_edit,name='product_variants_edit'),
    path('approved/options/config/edit',product_option_config_edit,name='product_option_config_edit'),
    # PRODUCT MASTER APPROVED EDIT RELATED APIS START /////
 
    # REVIEW APIS START /////
    path('review',review,name='review'),
    path('review/create',create_review,name='review_create'),
    path('review/get',review_get,name='review_get'),
    path('review/status',review_status,name='review_status'),
    path('review/reply',reply_review,name='reply_review'),
    # REVIEW APIS START /////
 
    # LEDGER APIS START /////
    path('ledger/get',ledger_get,name='ledger_get'),
    path('vendor/payout',process_vendor_payouts,name='payout_details_get'),
    path('vendor/payout/summary/get',vendor_payout_summary_get,name='vendor_payout_summary_get'),
    path('vendor/orders/summary/get',vendor_orders_summary_get,name='vendor_orders_summary_get'),
    path('order/items/get',order_sub_items_get,name='order_sub_items_get'),
    # LEDGER APIS START /////
 
    # PRODUCT HISTORY APIS START /////
    path('history/tracking/get',product_history_tracking,name='product_history_tracking'),
    # PRODUCT HISTORY APIS START /////
   
    # TAG MASTER START /////
    path('tag/create',tags_master,name='tag_master'),
    path('tag/get',tags_master_get,name='tag_master_get'),
    # TAG MASTER END ///////
 
    # LOGO MASTER START /////
    path('logo/create',logo_master,name='logo_master'),
    # LOGO MASTER END ///////
 
 
    # PAYOUT MASTER START /////
    path('payout/day/create',payout_day_create,name='payout_day_create'),
    path('payout/day/get',payout_day_get,name='payout_day_get'),
    # PAYOUT MASTER END ///////
]