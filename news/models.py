from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce

class Author(models.Model):
    """ Модель, содержащая объекты всех авторов. """

    # Связь «один к одному» с встроенной моделью пользователей User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Рейтинг пользователя
    rating = models.IntegerField(default=0)

    # Метод update_rating(), который обновляет рейтинг пользователя, переданный в аргумент этого метода
    def update_rating(self):

        # Cуммарный рейтинг каждой статьи автора умножается на 3
        author_posts_rating = self.posts.aggregate(apr=Coalesce(Sum('rating'), 0))['apr']

        # Cуммарный рейтинг всех комментариев автора
        author_comments_rating = self.user.comments.aggregate(acr=Coalesce(Sum('rating'), 0))['acr']

        # Суммарный рейтинг всех комментариев к статьям автора
        author_posts_comments_rating = self.posts.aggregate(apcr=Coalesce(Sum('comment__rating'), 0))['apcr']

        self.rating = author_posts_rating * 3 + author_comments_rating + author_posts_comments_rating
        self.save()

class Category(models.Model):
    """ Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.). """

    # Категории новостей/статей
    name = models.CharField(max_length=255,
                            unique=True)

class Post(models.Model):
    """ Эта модель должна содержать в себе статьи и новости, которые создают пользователи.
    Каждый объект может иметь одну или несколько категорий. """

    # Cвязь «один ко многим» с моделью Author
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')

    # выбор типа постов
    article = 'ART'
    news = 'NEW'

    POSTS = [
        (article, "Статья"),
        (news, "Новость")
    ]

    # Поле с выбором — «статья» или «новость»
    type = models.CharField(max_length=3,
                            choices=POSTS,
                            default=article)

    # Автоматически добавляемая дата и время создания
    creation_time = models.DateTimeField(auto_now_add=True)

    # Cвязь «многие ко многим» с моделью Category
    title = models.CharField(max_length=255)

    # Заголовок статьи/новости
    text = models.TextField()

    # Текст статьи/новости
    rating = models.IntegerField(default=0)

    # Рейтинг статьи/новости
    category = models.ManyToManyField(Category, through='PostCategory')

    # Метод like, который увеличивает рейтинг поста на единицу
    def like(self):
        self.rating += 1
        self.save()

    # Метод dislike, который уменьшает рейтинг поста на единицу
    def dislike(self):
        self.rating -= 1
        self.save()

    # Метод preview, который возвращает начало статьи (предварительный просмотр)
    # длиной 124 символа и добавляет многоточие в конце
    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        return f"{self.title} {self.text}"

class Comment(models.Model):
    """ Под каждой новостью/статьёй можно оставлять комментарии,
    поэтому необходимо организовать их способ хранения тоже."""

    # Связь «один ко многим» со встроенной моделью User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    # Связь «один ко многим» с моделью Post
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # Текст комментария
    text = models.TextField()

    # Дата и время создания комментария
    creation_time = models.DateTimeField(auto_now_add=True)

    # Рейтинг комментария
    rating = models.IntegerField(default=0)

    # Метод like, который увеличивает рейтинг комментария на единицу
    def like(self):
        self.rating += 1
        self.save()

    # Метод dislike, который уменьшает рейтинг комментария на единицу
    def dislike(self):
        self.rating -= 1
        self.save()

class PostCategory(models.Model):
    """ Промежуточная модель для связи «многие ко многим» """

    # Связь «один ко многим» с моделью Post
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # Связь «один ко многим» с моделью Category
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
