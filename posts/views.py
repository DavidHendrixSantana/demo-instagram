
import imp
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from datetime import datetime
# from django.shortcuts import redirect, render
# from users.views import login_view
from posts.forms import PostForm
from posts.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView ,CreateView

class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


# Metodo tradicional para enviar los POSTS
# @login_required
# def list_posts(request):
#     posts = Post.objects.all().order_by('-created')
#     return render(request, 'posts/feed.html', {'posts': posts})

class PostDetailView(LoginRequiredMixin, DetailView):

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

# Create Post using  Create View Django Funciton
class CreatePostView(LoginRequiredMixin, CreateView):
    # Create a new post.
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context


# Creates Post Method 
# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts:feed')
#     else:
#         form = PostForm()
#     return render(
#         request=request,
#         template_name='posts/new.html',
#         context={
#             'form':form,
#             'user': request.user,
#             'profile': request.user.profile
#         })