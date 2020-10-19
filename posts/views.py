from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CreatePostForm

# Create your views here.

def index(request):

    context ={
        "posts": Post.objects.all(),
        
    }
    return render(request, "posts/index.html",context)

def myPost(request):

    return

def createPost(request):

    if request.method == "POST":
        form = CreatePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    
    else:
        form = CreatePostForm()

    context = {
        "form": form,
    }


    return render(request, 'posts/create-post.html',context)
def postDetail(request, pk):
    post = Post.objects.get(id = pk)
    comments = post.comment_set.all()
    context ={
        "post": Post.objects.get(id = pk),
        "comments": comments
    }
    return render(request, "posts/post-detail.html", context)



def aboutUs(request):

    return

def profile(request):

    return



