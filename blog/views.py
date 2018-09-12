from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm, LoginForm
from django.contrib.auth import logout, login, authenticate

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True)
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def publish(self):
    self.published_date = timezone.now()
    self.save()

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def login_logic(request):
    username = request.POST['username']
    password = request.POST['password']
    user = login(user=request.user, request=request, backend='django.contrib.auth.backends.ModelBackend')
    
def logout_logic(request):
    logout(request)
    return redirect('post_list')

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return True
    else:
        return False

def display_login_view(request):
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def login_view(request):
    if(request.user.is_authenticated):
        logout(request)
        return redirect('post_list')
        
    if request.method == "POST":
        form = LoginForm(request.POST)
#        import pdb; pdb.set_trace()
        if form.is_valid():
            if login_user(request):
                form.save(commit=False)
                return redirect('post_list')
            
    return display_login_view(request)