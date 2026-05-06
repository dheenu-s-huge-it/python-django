from django.urls import path
from .views import get_about, get_contact, get_homepage_post, get_post_details

app_name = "app"

urlpatterns = [
    path("", get_homepage_post, name="get_home"),
    path("homepage/", get_homepage_post, name="homepage"),
    path("about/", get_about, name="about"),
    path("contact/", get_contact, name="contact"),
    path("details/<int:id>/", get_post_details, name="post_details"),
]
