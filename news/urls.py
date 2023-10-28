from django.urls import path
# Импортируем созданные нами представления
from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('search/', PostSearch.as_view(), name = 'post_search'),
   path('create/', PostCreate.as_view(), name = 'post_create'),
   path('create/<int:pk>', PostUpdate.as_view(), name = 'post_update'),
   path('delete/<int:pk>', PostDelete.as_view(), name = 'post_delete'),
]