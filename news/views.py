from datetime import datetime
from typing import Dict, Any

from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import View

from django.shortcuts import render, get_object_or_404

from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class PostList(ListView):
    model = Post
    ordering = 'creation_time'
    template_name = 'news_app/news_list.html'
    context_object_name = 'news_all'
    paginate_by = 1
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = Post.objects.all()
        context['form'] = PostForm()
        context['category'] = Post.category
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

class PostCreate(PermissionRequiredMixin, CreateView):
    template_name = 'news_app/news_create.html'
    form_class = PostForm
    permission_required = ('news.create_post')

class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    template_name = 'news_app/news_create.html'
    form_class = PostForm
    permission_required = ('news.update_post')

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

class CategoryList(ListView):
    model = Post
    template_name = 'news_app/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(category=self.category).order_by('creation_time')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscribed'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        context['news'] = Post.objects.all()
        return context

def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = "Теперь вы подписаны на категорию"
    return render(request, 'news_app/subscribe.html', {'category': category, 'message': message})
