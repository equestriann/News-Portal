from datetime import datetime

from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View

from django.shortcuts import render

from .models import Post
from .filters import PostFilter
from .forms import PostForm

class PostList(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news_app/news_list.html'
    context_object_name = 'news_all'
    paginate_by = 1
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return super().get(request, *args, **kwargs)

class PostSearch(ListView):
    model = Post
    ordering = '-creation_time'
    template_name = 'news_app/news_search.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'news_app/news_detail.html'
    context_object_name = 'news'

class PostCreate(CreateView):
    template_name = 'news_app/news_create.html'
    form_class = PostForm

class PostUpdate(UpdateView):
    template_name = 'news_app/news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id_ = self.kwargs.get('pk')
        return Post.objects.get(pk=id_)

class PostDelete(DeleteView):
    template_name = 'news_app/news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

class Posts(View):
    def get(self, request):
        posts = Post.objects.order_by('-rating')
        p = Paginator(posts, 1)
        posts = p.get_page(request.GET.get('page', 1))
        data = {
            'posts': posts,
        }
        return render(request, 'news_app/news_search.html', data)
