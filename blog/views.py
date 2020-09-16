from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.http import Http404
from .forms import  BloPostModelForm
from django.contrib.admin.views.decorators import staff_member_required


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

@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use a form
    form = BloPostModelForm(request.POST or None)
    print(form)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.user = request.user
        obj.save()
        # print(form.cleaned_data)
        # title = form.cleaned_data['title']
        # content= form.cleaned_data['content']
        # slug= form.cleaned_data['slug']
        # obj= BlogPost.objects.create(title=title,content=content,slug=slug)
        # obj=BlogPost()
        # obj.title
        # =title
        # obj.content=content
        # obj.slug=slug
        # obj.save()
        form=BloPostModelForm()
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
