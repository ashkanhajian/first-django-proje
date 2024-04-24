from django import template
from ..models import Post, Comment
from django.db.models import Count
from markdown import markdown
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag()
def total_posts():
    return Post.Published.count()


@register.simple_tag()
def total_comments():
    return Comment.objects.filter(active=True).count()


@register.simple_tag()
def last_post():
    return Post.Published.last().publish


@register.inclusion_tag("partials/latestposts.html")
def latest_posts(count=4):
    l_posts = Post.Published.order_by('-publish')[:count]
    context = {'l_posts': l_posts}
    return context


@register.simple_tag()
def fav_post(count=5):
    return Post.Published.annotate(comments_count=Count('comments')).order_by("-comments_count")[:count]


@register.filter(name='markdown')
def to_markdown(text):
    return mark_safe(markdown(text))
