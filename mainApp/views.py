from django.shortcuts import render
from .models import Post

# Create your views here.

def home_view(request):
    cur_user = request.user
    return render(request, 'BaseSite.html', context={"cur_user":cur_user})

def index_view(request):
    all_posts = Post.objects.all()
    cur_user = request.user
    return render(request, 'index.html', context={"all_posts":all_posts, "cur_user":cur_user})
