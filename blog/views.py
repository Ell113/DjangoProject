from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PostListView(generic.ListView):
    model = Post
    paginate_by = 5
    

class PostDetailView(generic.DetailView):
    model = Post

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:post_list')
    template_name = 'signup.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post

    fields = ['title', 'body', 'status']
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        slug = form.instance.title
        form.instance.slug = slug.replace(" ", "_")
        if form.instance.title != "" and form.instance.body != "" and form.instance.status != "":
            return super().form_valid(form)
        else:
            form.add_error('Wrong data!')
            return self.form_invalid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body', 'status']



class PostProfile(generic.ListView):
    model = Post
    template_name = 'profile.html'
