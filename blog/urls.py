from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name="blog"),
    path('<int:pk>/<slug:post>',
         views.post_detail, name='post_detail'),
    path('login', views.user_login, name="login"),
    path('register', views.SignUp.as_view(), name="register")

]
