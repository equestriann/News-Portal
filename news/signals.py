from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

from .models import PostCategory
from NewsPaper import settings

from .tasks import sendmail_once_postcreated

@receiver(m2m_changed, sender=PostCategory)
def notify_about_new_posts(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        pk = instance.pk
        sendmail_once_postcreated.delay(pk)
