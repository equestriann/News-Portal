from celery import shared_task
import time
import datetime

@shared_task
def weekly_mailing():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(creation_time__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscibers = Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True)
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    message = EmailMultiAlternatives(
        subject='Новые публикации',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscibers
    )

    message.attach_alternative(html_content, 'text/html')
    message.send()