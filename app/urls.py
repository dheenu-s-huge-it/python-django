from django.urls import path
from .views import (
    get_about,
    get_contact,
    HomepagePostView,
    PostDetailView,
    app_login,
    app_register,
    # create_post,
    # update_post,
    # delete_post
    CreatePostView,
    UpdatePostView,
    DeletePostView
    
)

app_name = "app"

# Function + Class Based URL patterns

urlpatterns = [
    path("", HomepagePostView.as_view(), name="get_home"),  # class based url pattern
    path(
        "homepage/", HomepagePostView.as_view(), name="homepage"
    ),  # class based url pattern
    path("about/", get_about, name="about"),
    path("contact/", get_contact, name="contact"),
    path("post_detail/<slug:slug>/", PostDetailView.as_view(), name="post_details"),
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("update_post/<slug:slug>/", UpdatePostView.as_view(), name="update_post"),
    path("post_delete/<slug:slug>/", DeletePostView.as_view(), name="delete_post"),
    path("login/", app_login, name="app_login"),
    path("register/", app_register, name="app_register"),
]

# Function Based URL patterns

# urlpatterns = [
#     path("", get_homepage_post, name="get_home"),
#     path("homepage/", get_homepage_post, name="homepage"),
#     path("about/", get_about, name="about"),
#     path("contact/", get_contact, name="contact"),
#     path("details/<int:id>/", get_post_details, name="post_details"),
# ]


# Class Based URL patterns

# urlpatterns = [
#     path("", HomepagePostView.as_view(), name="get_home"),
#     path("homepage/", HomepagePostView.as_view(), name="homepage"),
#     path("about/", AboutpageView.as_view(), name="about"),
#     path("contact/", ContactView.as_view(), name="contact"),
#     path("details/<int:id>/", get_post_details, name="post_details"),
# ]
