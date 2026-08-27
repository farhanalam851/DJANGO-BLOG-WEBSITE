from django.urls import path
from . import views
from user.views import PostListView , PostCreateView , PostDetailView ,PostDeleteView, PostUpdateView , UserPostListView

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view() , name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view() , name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view() , name='post-delete'),
    path('post/new/' , PostCreateView.as_view() , name='post-create'),
    path('about/',views.about,name='blog-about'),
     path('announcements/', views.announcements, name='announcements'),
    path('calendar/', views.calendar, name='calendar'),
    path('more/', views.more, name='more'),
    path('post/<int:pk>/like/', views.like_post, name='like-post'),
]