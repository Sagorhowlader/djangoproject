from django import forms
from .models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    slug = forms.SlugField()


class BloPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'slug']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title_ixact=title)
        if qs.exists():
            raise forms.ValidationError('This title already use')
        return title
