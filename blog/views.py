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