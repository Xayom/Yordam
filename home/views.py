from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from home.forms import LoginForm
from post.models import Post

app_name = 'home'


def home(request):
    template_name = 'home.html'
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return redirect('home')  # Redirect to a success page.

    post = Post.objects.filter(post_status=1)
    return render(request, template_name, context={'posts': post, 'form': form})
