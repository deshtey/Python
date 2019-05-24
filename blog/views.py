from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views import generic
from .forms import CommentForm


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    template_name = 'blog/post/list.html'


def post_detail(request, pk, post):
    post = get_object_or_404(
        Post, id=pk, slug=post)
    comments = post.comments.filter(approved=True)
    new_comment = None
    if request.method == 'POST':

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})
