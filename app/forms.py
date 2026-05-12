from django import forms
from .models import Post

from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ["title", "body", "category", "published"]

        labels = {"title": "Post Name", "body": "Post Description"}

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Enter post title"}
            ),
            "body": forms.Textarea(attrs={"class": "form-textarea", "rows": 5}),
            "category": forms.Select(attrs={"class": "form-select"}),
            "published": forms.CheckboxInput(attrs={"class": "form-checkbox"}),
        }

    # Custom validation
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title:
            if len(title) < 3:
                raise forms.ValidationError("Title must be at least 3 characters")
        return title

    def clean_body(self):
        body = self.cleaned_data.get("body")
        if body:
            if len(body) > 1000:
                raise forms.ValidationError(
                    "Maximum characters reached. Characters must be below 100"
                )
        return body


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-input", "placeholder": "Enter you email"}
        )
    )


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Enter new password"}
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-input", "placeholder": "Confirm password"}
        )
    )

    def clean(self):

        cleaned_data = super().clean()

        new_password = cleaned_data.get("new_password")

        confirm_password = cleaned_data.get("confirm_password")

        if new_password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data
