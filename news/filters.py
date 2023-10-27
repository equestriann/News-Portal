from django_filters import FilterSet, DateFilter
from .models import Post

from django import forms


class PostFilter(FilterSet):
    date = DateFilter(
        widget=forms.DateInput(format='%d %M %Y',
                               attrs={'type': 'date'}),
        field_name='creation_time',
        lookup_expr='date__gte',
        label = 'Позже этой даты:',
    )

    class Meta:
        model = Post
        fields = {
            'author__user': ['exact'],
        }
