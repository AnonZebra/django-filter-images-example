from django.shortcuts import render
from .models import BlogPost, Image

def blog_detail(request, pk):
    blogpost = BlogPost.objects.get(pk=pk)
    myimages_objs = blogpost.image_set.all()
    context = {
        'blogpost': blogpost,
        'myimages_objs': myimages_objs,
    }
    return render(request,
                  template_name='blog/blog_detail.html',
                  context=context)


def blog_list(request):
    blogposts = BlogPost.objects.all()
    context = {
        'blogposts': blogposts,
    }
    return render(request,
                  template_name='blog/blog_list.html',
                  context=context)
