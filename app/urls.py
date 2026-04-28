from django.urls import path
from .views import get_home, get_about, get_contact

app_name = "app"

urlpatterns = [
    path("", get_home, name="get_home"),
    path("about/", get_about, name="about"),
    path("contact/", get_contact, name="contact"),
]
