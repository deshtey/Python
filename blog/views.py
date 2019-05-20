from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views import generic


def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, pk, post):
    post = get_object_or_404(
        Post, id=pk, slug=post)
    return render(request, 'blog/post/detail.html', {'post': post})
