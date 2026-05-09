from django.db import models

from django.utils.text import slugify

from django.urls import reverse


# Create your models here.


class Categories(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True, unique=True)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Posts"


class Details(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Details"
        
    def get_absolute_url(self):

        return reverse(
        "app:post_details",
        kwargs={"slug": self.slug}
    )



class Tags(models.Model):
    name = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"


class Comments(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=10000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Comments"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact"


class About(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=12000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "About"
