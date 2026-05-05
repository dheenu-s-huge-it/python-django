from django.shortcuts import render

from django.http import HttpResponse

from app.models import Post, About, Contact, Details

# Create your views here.


def get_homepage(request):
    posts = Post.objects.all()
    # posts = Post.objects.all().filter(published=True).order_by('-created_at')[:2] - multi chaining data
    return render(request, "app/home.html", {"posts": posts})


def get_homepage_filtered(request):
    posts = Post.objects.filter(published=True)
    return render(request, "app/home.html", {"posts": posts})


def get_about(request):
    about = About.objects.all()
    return render(request, "app/about.html", {"about": about})


def get_contact(request):
    contact = Contact.objects.all()
    return render(request, "app/contact.html", {"contact": contact})

def get_post_details(request, ):
    post_details = Details.objects.get(title="python")
    return render(request, "app/post_details.html", {"post_details": post_details})

