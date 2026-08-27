from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
# Create your views here.




def home(request):
    context = {
        'posts': Posts.objects.all()
    }
    return render (request , 'blogs/home.html' , context)

def about(request):
    return render (request , 'blogs/about.html' , {'title': 'About'})

def announcements(request):
    return render(request, 'blogs/announcements.html')


def calendar(request):
    return render(request, 'blogs/calendar.html')


def more(request):
    return render(request, 'blogs/more.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Posts, Like


@login_required
def like_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()

    return redirect('post-detail', pk=post.pk)