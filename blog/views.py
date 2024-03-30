from django import forms
from django.shortcuts import render, get_object_or_404, redirect

from .forms import AuthorForm, PostForm, CommentForm, EditPostForm
from .models import Author, Post, Comment


def authors_posts(request, author_id):
    posts = Post.objects.filter(author__pk=author_id)
    return render(request, 'blog/index.html', {'posts': posts})
    # author = get_object_or_404(Author, pk=author_id)
    # posts = Post.objects.filter(author=author).order_by('-id')


def read_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                author=data['author'],
                post=post,
                content=data['content'],
            )
            return redirect('read_post', post_id)
    else:
        form = CommentForm()
    context = {
        'post_id': post.pk,
        'post_title': post.title,
        'post_pub': post.pub_date,
        'post_content': post.content,
        'post_author': post.author,
        'post_category': post.category,
        'post_views_count': post.views_count,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/post.html', context)


def aurhor_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        post = Post.objects.filter(pk=post_id).first()
        form.title = forms.CharField(widget=forms.TextInput(attrs={'value': post.title}))
        if form.is_valid():
            form.save()
            return redirect('author_form')
    else:
        form = AuthorForm()
    return render(request, 'blog/author_form.html', {'form': form})


def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                title=data['title'],
                content=data['content'],
                pub_date=data['pub_date'],
                author=data['author'],
                category=data['category'],
                views_count=data['views_count'],
                is_public=data['is_public'],
            )
            return redirect('post_form')
    else:
        form = PostForm()
    return render(request, 'blog/author_form.html', {'form': form})

def edit_post(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    if request.method == 'POST':
        form = EditPostForm(post_id,request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post.title=data['title']
            post.save()
                # content=data['content'],
                # pub_date=data['pub_date'],
                # author=data['author'],
                # category=data['category'],
                # views_count=data['views_count'],
                # is_public=data['is_public'],
            return redirect('read_post', post_id)
    else:
        form = EditPostForm(post_id)
    return render(request, 'blog/author_form.html', {'form': form, 'post': post})