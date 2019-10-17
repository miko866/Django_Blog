from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


def home(request):  # Home page
    context = {
        # Take all data from DB
        'posts': Post.objects.all()
    }
    # Return template with the DB data
    return render(request, 'blog/home.html', context)


class PostListView(ListView):  # For better show in Home page als Python List
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # Newest Post is First
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post


# LoginRequiredMixin inherit Login class only Logged can created new post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # befor submit take the author id
        form.instance.author = self.request.user
        # override base method with author and form validation
        return super().form_valid(form)


# UserPassesTestMixin check only user owner the pOst can Updated the post not other user
class PostUpdateView(LoginRequiredMixin,  UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):  # befor submit take the author id
        form.instance.author = self.request.user
        # override base method with author and form validation
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # check the current User is author from the post
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,  UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # check the current User is author from the post
        if self.request.user == post.author:
            return True
        return False


def contact(request):   # Contact page
    return render(request, 'blog/contact.html', {'title': 'Contact'})
