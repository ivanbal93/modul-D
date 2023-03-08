from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import NewsFilter
from .forms import NewPostForm
from django.urls import reverse_lazy

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-post_datetime'
    template_name = 'post_list.html'
    context_object_name = 'post_list'
    paginate_by = 10
    

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detailed.html'
    context_object_name = 'post_det'


class Search(PostList):
    template_name = 'search.html'
    # context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewPost(CreateView):
    form_class = NewPostForm
    model = Post
    template_name = 'newpost.html'


class PostUpdate(UpdateView):
    form_class = NewPostForm
    model = Post
    template_name = 'newpost.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('post_list')
