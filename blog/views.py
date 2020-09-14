from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404
from .forms import  Blog_Create_Post


# Create your views here.
def blog_post_details_page(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)

    # queryset= BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #     raise Http404
    # obj = queryset.first()
    template_name = 'blog/post_detail.html'
    context = {"object": obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    # list out objects
    # cloud be search
    qs = BlogPost.objects.all()
    template_name = 'blog/post_list.html'
    context = {"object_list": qs}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # create objects
    # ? use a form
    form = Blog_Create_Post(request.POST or None)

    if form.is_valid():
        obj = Blog_Create_Post.objects.create(**form.cleaned_data)
        form = Blog_Create_Post()
    template_name = 'form.html'
    context = {"form": form}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # 1 oject-> details view

    template_name = 'blog/post_detail.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"objects": obj}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    template_name = 'blog/post_update.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"objects": obj, "form": None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    template_name = 'blog/post_deleted.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"objects": obj}
    return render(request, template_name, context)
