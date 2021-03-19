from django.shortcuts import reverse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    TemplateView,
)


from django.contrib.auth import views as auth_views
from django.contrib import messages


# LoginRequiredMixing => login required | UserPassesTestMixin => checking something for user
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post, Profile
from .forms import RegisterUserForm


# Create your views here.

# main page
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'todo/post_list.html'
    ordering = ['-up_date']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post
    template_name = 'todo/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'todo/post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        messages.add_message(self.request, messages.SUCCESS,
                             f'Post " {form.instance.title} " was created successfully !')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']
    template_name = 'todo/post_update.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.WARNING,
                             f'Post " {form.instance.title} " was updated successfully !')
        return super().form_valid(form)

    def test_func(self):
        # to get current post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'todo/post_delete.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        post_title = self.get_object().title
        messages.add_message(self.request, messages.WARNING, f'Post " {post_title} " deleted successfully !')
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        # to get current post
        post = self.get_object()
        if self.request.user == post.author:
            print('ACCESS')
            return True
        print('DECLINE')
        return False


class UserRegisterView(FormView):
    form_class = RegisterUserForm
    template_name = 'todo/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'todo/profile.html'
    success_url = reverse_lazy('home')


class UserPostsView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'todo/user_posts.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(author__id=self.kwargs['pk'])


