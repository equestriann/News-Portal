from django.urls import path
# Импортируем созданные нами представления
from .views import (PostList,
                    PostDetail,
                    PostSearch,
                    PostCreate,
                    PostUpdate,
                    PostDelete,
                    CategoryList,
                    subscribe)

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('search/', PostSearch.as_view(), name = 'post_search'),
   path('create/', PostCreate.as_view(), name = 'post_create'),
   path('create/<int:pk>', PostUpdate.as_view(), name = 'post_update'),
   path('delete/<int:pk>', PostDelete.as_view(), name = 'post_delete'),
   path('category/<int:pk>', CategoryList.as_view(), name = 'category_list'),
   path('category/<int:pk>/subscribe', subscribe, name = 'subscribe')
]