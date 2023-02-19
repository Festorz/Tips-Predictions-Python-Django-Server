from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from urllib.parse import quote
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Comment, Post
from .forms import CommentForm

# Create your views here.

def is_valid(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


def blog(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    recent_posts = Post.objects.all().order_by('pk')[:4]

    data = {
        'posts': page_obj,
        'recent_post': recent_posts,
    }
    query = request.GET.get('q', None)
    if query is not None:
        search = Post.objects.filter(title__icontains=query)
        paginator = Paginator(search, 10)
        page_obj = paginator.get_page(page_number)
        # print(search)
        data.update({
            'posts': page_obj
        })

    return render(request, 'blog.html', data)


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)
    share_string = quote(post.intro)
    recent_posts = Post.objects.all().order_by('-pk')[:4]

    if request.user.is_authenticated:
        post.views.add(request.user)
        post.save()

    data = {
        'post': post,
        'recent': recent_posts,
        'share_string': share_string
    }

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            website = form.cleaned_data.get('website')
            comment = form.cleaned_data.get('comment')

            if is_valid([name, email, comment]):
                cmnt = Comment(
                    post=post,
                    name=name,
                    email=email,
                    comment=comment,
                    website=website
                )
                cmnt.save()

            return redirect('blog:post-detail', slug=post.slug)
    return render(request, 'blog-single.html', data)


@login_required
def blog_like(request, slug):
    post = Post.objects.get(slug=slug)
    post.likes.add(request.user)
    post.save()

    return HttpResponseRedirect(reverse('blog:post-detail', args=[str(slug)]))
