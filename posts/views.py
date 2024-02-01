from django.shortcuts import render
from .models import Post, Comment


def posts(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request ,'posts.html', {"posts":posts})
