from django_filters import FilterSet, DateRangeFilter
from .models import Post

class PostFilter(FilterSet):
    creation_time = DateRangeFilter

    class Meta:
        model = Post
        fields = {
            'author__user' : ['exact'],
            'title' : ['icontains'],
            'creation_time' : ['gt'],
        }