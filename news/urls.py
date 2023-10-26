from django.urls import path
# Импортируем созданные нами представления
from .views import PostList, PostDetail, PostSearch

urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
   path('search/', PostSearch.as_view()),
]