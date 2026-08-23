from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
     path('announcements/', views.announcements, name='announcements'),
    path('calendar/', views.calendar, name='calendar'),
    path('more/', views.more, name='more'),
]