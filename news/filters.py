from django_filters import FilterSet, DateFilter
from .models import Post

class PostFilter(FilterSet):
    creation_time = DateFilter

    class Meta:
        model = Post
        fields = {
            'author__user' : ['exact'],
            'title' : ['icontains'],
            'creation_time' : ['gt'],
        }