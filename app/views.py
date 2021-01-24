import json
import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader_tags import register

from app.forms import PostForm
from app.models import Post, Comment


def home_view(request):
    if request.method == 'GET':
        post_form = PostForm()
    elif request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            obj = post_form.save(commit=False)
            obj.user_fk = request.user
            obj.save()
    return render(request, 'app/home.html', context={'post_form': post_form})


def post_comment(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    try:
        body = json.loads(request.body)
    except json.JSONDecodeError:
        return HttpResponse(status=400)
    if 'comment' not in body or 'post_id' not in body:
        return HttpResponse(status=400)
    comment = body['comment']
    post_id = body['post_id']
    Comment.objects.create(
        comment_text=comment,
        user_fk=request.user,
        post_fk_id=post_id
    )
    return render(request, "app/comments.html", context=show_comments(Post.objects.get(pk=post_id), True))


@register.inclusion_tag('app/comments.html')
def show_comments(post, latest):
    comments = post.comment_set.all()
    return {'comments': comments.order_by("id")} if not latest else {'comments': [comments.order_by("id").reverse()[0]]}


@register.inclusion_tag('app/posts.html')
def show_posts():
    posts = Post.objects.all()
    return {'posts': posts}
