from datetime import datetime

from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView
from django.views import View

from django.shortcuts import render

from .models import Post
from .filters import PostFilter

class PostList(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news_all.html'
    context_object_name = 'news_all'
    paginate_by = 1

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
    #     return context

class PostSearch(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news_search.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news_one.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # title = context['title']
        # content = context['text']
        return context

class Posts(View):
    def get(self, request):
        posts = Post.objects.order_by('-rating')
        p = Paginator(posts, 1)
        posts = p.get_page(request.GET.get('page', 1))
        data = {
            'posts': posts,
        }
        return render(request, 'news_search.html', data)
