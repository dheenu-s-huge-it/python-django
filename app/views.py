from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpRequest
from app.models import Post, MyblogsTemp, Contact, Details, Categories

from django.core.paginator import Paginator

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .forms import PostForm
from django.urls import reverse, reverse_lazy

from .forms import RegistrationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Function Based views (FBV)

# def get_homepage_post(request):
#     posts = Post.objects.all().order_by("id")
#     categories = Categories.objects.all()
#     count = Post.objects.filter(published=True).count()

#     search_query = request.GET.get("search", "")
#     category_id = request.GET.get("category", "")

#     if search_query:
#         posts = posts.filter(title__icontains=search_query).order_by("id")

#     if category_id:
#         posts = posts.filter(category_id=category_id)

#     # pagination
#     paginator = Paginator(posts, 5)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     # page_obj hold actual posts, has_next(), has_previous(), next_page_number(), previous_page_number()

#     return render(
#         request,
#         "app/home.html",
#         {
#             "posts": page_obj,
#             "categories": categories,
#             "count": count,
#             "page_obj": page_obj,
#         },
#     )
#     # posts = Post.objects.all().filter(published=True).order_by('-created_at')[:2] - multi chaining data


class HomepagePostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "app/home.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        posts = Post.objects.all().order_by("id")

        search_query = self.request.GET.get("search", "")
        category_id = self.request.GET.get("category", "")

        if search_query:
            posts = posts.filter(title__icontains=search_query)

        if category_id:
            posts = posts.filter(category_id=category_id)

        print(self.request.user)
        return posts.select_related(
            "category"
        )  # it perform SQL joins and fetch the data from the database

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["categories"] = Categories.objects.all()
        context["count"] = Post.objects.filter(published=True).count()

        return context


@login_required
def get_myblogs(request):
    myblogs = MyblogsTemp.objects.all()
    return render(request, "app/myblogs.html", {"myblogs": myblogs})


@login_required
def get_contact(request):
    contact = Contact.objects.all()
    return render(request, "app/contact.html", {"contact": contact})


# def create_post(request):

#     if request.method == "POST":
#         form = PostForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect("app:homepage")

#     else:
#         form = PostForm()

#     return render(request, "app/create_post.html", {"form": form})


# def update_post(request, slug):

#     post = get_object_or_404(Post, slug=slug)

#     if request.method == "POST":
#         form = PostForm(request.POST, instance=post)

#         if form.is_valid():
#             form.save()

#             return redirect("app:homepage")

#     else:
#         form = PostForm(instance=post)

#     return render(request, "app/update_post.html", {"form": form})


# def delete_post(request, slug):

#     post = get_object_or_404(Post, slug=slug)

#     if request.method == "POST":
#         post.delete()
#         return redirect("app:homepage")
#     return render(request, "app/delete_post.html", {"post": post})


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "app/create_post.html"
    success_url = reverse_lazy("app:homepage")

    # ownership of creating posts
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "app/update_post.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    # def get_success_url(self):
    #     return reverse_lazy("app:homepage", kwargs={"slug": self.object.slug})

    success_url = reverse_lazy("app:homepage")

    # ownership of update access
    
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    form_class = PostForm
    template_name = "app/update_post.html"
    context_object_name = "post"
    success_url = reverse_lazy("app:homepage")
    slug_field = "slug"
    slug_url_kwarg = "slug"
    
    # ownership of delete access
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


def register_user(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        # This handles the initial GET request when the user first visits the page
        form = RegistrationForm()

    # This return is OUTSIDE the if/else blocks so it always runs
    return render(request, "registration/register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(
                request, user
            )  # creates the session id or key, send to browser and stored in cookies
            return redirect("app:homepage")
    else:
        form = AuthenticationForm()
    return render(request, "registration/login.html", {"form": form})


@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("app:login_user")
    return redirect("app:homepage")


# Without 404 Error handling return multiple objects

# def get_post_details(request, id):
#     details = Details.objects.get(post_id=id)
#     return render(request, "app/details.html", {"details": details})


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "app/details.html"
    context_object_name = "details"
    slug_url_kwarg = "slug"
    slug_field = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["details"] = Details.objects.filter(post=self.object).order_by("id")

        return context


# With 404 Error handling return a single object (especially for slugs)

# def get_post_details(request, id):
#     details = get_object_or_404(Details, post_id=id)  # 404 best practice
#     # details = get_object_or_404(Details, post_id=id, published=True)
#     return render(request, "app/details.html", {"details": details})


# Class Based views (FBV)

# class HomepagePostView(ListView):
#     model = Post
#     template_name = "app/home.html"
#     context_object_name = "posts"
#     paginate_by = 5

#     def get_queryset(self):
#         posts = Post.objects.all().order_by("id")

#         search_query = self.request.GET.get("search", "")
#         category_id = self.request.GET.get("category", "")

#         if search_query:
#             posts = posts.filter(title__icontains=search_query)

#         if category_id:
#             posts = posts.filter(category_id=category_id)

#         return posts.select_related("category")     # it perform SQL joins and fetch the data from the database

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         context["categories"] = Categories.objects.all()
#         context["count"] = Post.objects.filter(published=True).count()

#         return context
