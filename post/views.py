from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView
from django.views.generic import DetailView

from post.models import Post, Comment
from post.forms import PostForm, CommentForm

app_name = 'post'


def add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.post_date = timezone.now()
            post.post_status = 0
            post.save()
            return redirect('post:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'add.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_date = timezone.now()
            post.save()
            return redirect('post:post_detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET' and post.post_author != request.user and post.post_status == 1:
        post.post_visits += 1
        post.save()

    if (request.GET.get('DeleteComment')):
        Comment.objects.filter(id=request.GET.get('DeleteComment')).delete()
        return redirect('post:post_detail', post.id)

    context = {}
    context['post'] = post
    context['comments'] = post.comment_set.all()
    comment_form = CommentForm
    context['form'] = comment_form

    return render(
        request,
        'post_detail.html',
        context=context
    )


def moderation(request):
    post = Post.objects.filter(post_status=0)
    if (request.GET.get('DeleteButton')):
        Post.objects.filter(id=request.GET.get('DeleteButton')).delete()
        return redirect('post:moderation')

    if (request.GET.get('checked')):
        post = Post.objects.get(id=request.GET.get('checked'))
        post.post_status = 1
        post.save()
        return redirect('post:moderation')
    return render(request, 'moderation.html', {'post': post})


@login_required
@require_http_methods(["POST"])
def add_comment(request, article_id):
    form = CommentForm(request.POST)
    post = get_object_or_404(Post, id=article_id)

    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.post_id = post
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()

    return redirect(post.get_absolute_url())

