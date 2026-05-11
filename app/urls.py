from django.urls import path
from .views import (
    get_myblogs,
    get_contact,
    HomepagePostView,
    PostDetailView,
    CreatePostView,
    UpdatePostView,
    DeletePostView,
    
    register_user,
    login_user,
    logout_user
)

app_name = "app"

# Function + Class Based URL patterns

urlpatterns = [
    path("", login_user, name="login_user"), 
    path("login/", login_user, name="login_user"),
    path("register/", register_user, name="register_user"),
    path("logout/", logout_user, name="logout_user"),
    path(
        "homepage/", HomepagePostView.as_view(), name="homepage"
    ),
    path("myblogs/", get_myblogs, name="myblogs"),
    path("contact/", get_contact, name="contact"),
    path("post_detail/<slug:slug>/", PostDetailView.as_view(), name="post_details"),
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("update_post/<slug:slug>/", UpdatePostView.as_view(), name="update_post"),
    path("post_delete/<slug:slug>/", DeletePostView.as_view(), name="delete_post"),
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
