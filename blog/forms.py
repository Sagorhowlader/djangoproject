from django import forms


class Blog_Create_Post(forms.Form):
    title = forms.CharField()
    Content = forms.CharField(widget=forms.Textarea)
    Slug = forms.SlugField()
