from django.urls import path
from . import views


urlpatterns = [

    path("", views.index, name="index"),
    path("post/<int:pk>/view", views.postDetail, name="post-detail"),
    path("post/new/create", views.createPost, name='create-post')
]