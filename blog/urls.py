from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name="blog"),
    path('<int:pk>/<slug:post>',
         views.post_detail, name='post_detail')
]
