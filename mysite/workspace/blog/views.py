from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', { 'posts': posts })

def getpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/getpost.html', { 'post': post})
