from django.urls import path
from .views import get_about, get_contact, get_homepage, get_post_details, get_homepage_filtered

app_name = "app"

urlpatterns = [
    path("", get_homepage, name="get_home"),
    path("homepage/", get_homepage, name="homepage"),
    path("homepage/filtered/", get_homepage_filtered, name="homepagefiltered"),
    path("about/", get_about, name="about"),
    path("contact/", get_contact, name="contact"),
    path("post_details/", get_post_details, name="details"),
]
