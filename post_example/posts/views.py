from django.shortcuts import redirect, render

from posts.forms import PostForm
from posts.models import Post

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'posts/index.html', context={'posts': posts})

def create(request):
    if request.method == 'GET':
        return render(request, 'posts/create.html', context={'form': PostForm()})
    if request.method == 'POST':
        # title, content = request.POST['title'], request.POST['content']
        # post = Post.objects.create(title=title, content=content)
        form = PostForm(request.POST)
        post = form.save()
        return redirect('post', id=post.id)

def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/post.html', context={'post': post})
