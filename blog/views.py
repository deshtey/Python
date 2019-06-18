from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment
from django.views import generic
from .forms import CommentForm, LoginForm, SignUpForm
from django.contrib.auth import authenticate, login


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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userData = form.cleaned_data
            user = authenticate(
                request, username=userData['username'], password=userData['password'])
            if user is not None:
                if user.is_active:
                    print(user)
                    login(request, user)

    else:
        form = LoginForm()

    return render(request, 'blog/account/login.html', {'form': form})


"""def signup(request):
    if request == "POST":
        pass
    else:
        sign_up_form = SignUpForm()
    return render(request, 'blog/account/register.html', {'form': sign_up_form})"""


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "blog/account/register.html"
