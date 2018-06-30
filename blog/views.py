from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.utils import timezone
from django.views import View
from markdown import markdown

from .models import Post
from .forms import PostForm


def parse_markdown(text: str) -> str:
    return markdown(text, extensions=['codehilite(linenums=False)'])


# Create your views here.
class BlogListView(View):
    def get(self, request):
        posts = Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')
        for p in posts:
            p.text = parse_markdown(p.text)
        return render(request, "blog/post_list.html", {"posts": posts})


class BlogDetailView(View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        post.text = parse_markdown(post.text)
        return render(request, "blog/post_detail.html", {"post": post})


class NewPostView(View):
    def get(self, request):
        form = PostForm()
        return render(request, "blog/post_edit.html", {"form": form})

    def post(self, request: HttpRequest):
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail_view', post_id=post.pk)
        return render(request, 'blog/post_edit.html', {'form': form})


class EditPost(View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = PostForm(instance=post)
        return render(request, "blog/post_edit.html", {"form": form})

    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = PostForm(data=request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail_view', post_id=post.pk)
        return render(request, 'blog/post_edit.html', {'form': form})
