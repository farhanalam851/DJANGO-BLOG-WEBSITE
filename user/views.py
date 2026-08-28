from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from . forms import UserRegistrationForm , UserUpdateForm ,ProfileUpdateForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ( ListView , DeleteView , UpdateView ,DetailView ,CreateView )
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from blog.models import Posts
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your Account has been created! You are Welcome. ")
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html' , {'form' : form})

def logout_view(request):
    logout(request)
    return render (request , 'users/logout.html')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'YOUR PRFILE HAS BEEN UPDATED')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(
        request,
        'users/profile.html',
        context
    )

class PostListView(ListView):
    model = Posts
    template_name = 'blogs/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5

class UserPostListView(ListView):
    model = Posts
    template_name = 'blogs/home.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-published_date')

class PostDetailView(DetailView):
    model = Posts
    template_name = 'blogs/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView ):
    model = Posts    
    template_name = 'blogs/post_form.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin,UpdateView ):
    model = Posts    
    template_name = 'blogs/post_form.html'
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'blogs/post_confirm_delete.html'
    model = Posts
    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


    
