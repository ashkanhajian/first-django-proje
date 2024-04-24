from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import *
from .form import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DeleteView
from django.views.decorators.http import require_POST

from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity


# Create your views here.

def index(request):
    return render(request, 'blog/index.html')


# def post_list(request):
# posts = Post.Published.all()
# paginator = Paginator(posts, 4)
# page_number = request.GET.get('page', 1)
# try:
# posts = paginator.page(page_number)
# except EmptyPage:
# posts = paginator.page(page_number)
# except PageNotAnInteger:
# posts = paginator.page(1)
# context = {
# 'posts': posts,
# }
# return render(request, 'blog/list.html', context)
class PostListView(ListView):
    queryset = Post.Published.all()
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/list.html"


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()

    context = {
        "post": post,
        'form': form,
        "comments": comments
    }
    return render(request, "blog/detail.html", context)


# class PostDetailView(DeleteView):
#     model = Post
#     template_name = "blog/detail.html"


def ticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            cd = form.cleaned_data
            ticket_obj.message = cd['message']
            ticket_obj.name = cd['name']
            ticket_obj.email = cd['email']
            ticket_obj.phone = cd['phone']
            ticket_obj.subject = cd['subject']
            ticket_obj.save()
            return redirect('blog:index')
    else:
        form = TicketForm()
    return render(request, 'forms/ticket.html', {'form': form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    context = {
        'post': post,
        'form': form,
        "comment": comment

    }
    return render(request, 'forms/comment.html', context)


def creat_post(request):
    if request.method == 'POST':
        form = CreatPost(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            img1 = Images.objects.create(image_file=form.cleaned_data['image1'], post=post)
            post.images.add(img1)

            return redirect('blog:profile')

    else:
        form = CreatPost()
    return render(request, 'forms/creatpost.html', {"form": form})


def post_search(request):
    query = None
    results = []
    if "query" in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results1 = Post.Published.annotate(similarity=TrigramSimilarity('title', query)) \
                .filter(similarity__gt=0.1).order_by('-similarity')
            results2 = Post.Published.annotate(similarity=TrigramSimilarity('description', query)) \
                .filter(similarity__gt=0.1).order_by('-similarity')
            results = (results1 | results2).order_by('-similarity')

    context = {
        'query': query,
        'results': results
    }
    return render(request, 'blog/search.html', context)


def profile(request):
    user = request.user
    posts = Post.Published.filter(author=user)
    context = {
        'posts': posts,
        'user': user

    }
    return render(request, 'blog/profile.html', context)
