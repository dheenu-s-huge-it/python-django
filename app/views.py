from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from app.models import Post, About, Contact, Details, Categories

from django.core.paginator import Paginator


def get_homepage_post(request):
    posts = Post.objects.all().order_by("id")
    categories = Categories.objects.all()
    count = Post.objects.filter(published=True).count()

    search_query = request.GET.get("search", "")
    category_id = request.GET.get("category", "")

    if search_query:
        posts = posts.filter(title__icontains=search_query).order_by("id")

    if category_id:
        posts = posts.filter(category_id=category_id)

    # pagination
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) 
    
    # page_obj hold actual posts, has_next(), has_previous(), next_page_number(), previous_page_number()

    return render(
        request,
        "app/home.html",
        {
            "posts": page_obj,
            "categories": categories,
            "count": count,
            "page_obj": page_obj,
        },
    )
    # posts = Post.objects.all().filter(published=True).order_by('-created_at')[:2] - multi chaining data


def get_about(request):
    about = About.objects.all()
    return render(request, "app/about.html", {"about": about})


def get_contact(request):
    contact = Contact.objects.all()
    return render(request, "app/contact.html", {"contact": contact})


# With 404 Error handling return a single object (especially for slugs)


def get_post_details(request, id):
    details = get_object_or_404(Details, post_id=id)  # 404 best practice
    # details = get_object_or_404(Details, post_id=id, published=True)
    return render(request, "app/details.html", {"details": details})


# Without 404 Error handling return multiple objects

""" def get_post_details(request, id):
    details = Details.objects(post_id=id).order_by(id)
    return render(request, "app/details.html", {"details": details})
 """
