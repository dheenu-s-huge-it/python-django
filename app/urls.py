from django.urls import path
from .views import (
    MyblogView,
    change_password,
    get_contact,
    HomepagePostView,
    PostDetailView,
    CreatePostView,
    UpdatePostView,
    DeletePostView,
    register_user,
    login_user,
    logout_user,
    forgot_password,
    reset_password,
    post_list_api,
    post_details_list_api,
    post_update,
    post_patch_update,
    post_delete,
    app_login,
    app_logout
)

app_name = "app"

# Function + Class Based URL patterns

urlpatterns = [
    path("", HomepagePostView.as_view(), name="homepage"),
    path("login/", login_user, name="login_user"),
    path("register/", register_user, name="register_user"),
    path("logout/", logout_user, name="logout_user"),
    path("change_password/", change_password, name="change_password"),
    path("forgot_password/", forgot_password, name="forgot_password"),
    path("reset-password/<uidb64>/<token>/", reset_password, name="reset_password"),
    path("homepage/", HomepagePostView.as_view(), name="homepage"),
    path("myblogs/", MyblogView.as_view(), name="myblogs"),
    path("contact/", get_contact, name="contact"),
    path("post_detail/<slug:slug>/", PostDetailView.as_view(), name="post_details"),
    path("create_post/", CreatePostView.as_view(), name="create_post"),
    path("update_post/<slug:slug>/", UpdatePostView.as_view(), name="update_post"),
    path("post_delete/<slug:slug>/", DeletePostView.as_view(), name="delete_post"),
    
    # API
    path("api/login/", app_login, name="app_login"),
    path("api/logout/", app_logout, name="app_logout"),
    path("api/get/posts/", post_list_api, name="post_list_api"),
    path("api/get/post/details/<slug:slug>", post_details_list_api, name="post_details_list_api"),
    path("api/post/update/<slug:slug>", post_update, name="post_update"),
    path("api/post/update/mono/<slug:slug>", post_patch_update, name="post_patch_update"),
    path("api/post/delete/<slug:slug>", post_delete, name="post_delete"),
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
