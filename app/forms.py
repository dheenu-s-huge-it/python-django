from django import forms
from .models import Post


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
