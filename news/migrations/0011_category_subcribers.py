# Generated by Django 4.2.6 on 2023-10-31 23:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0010_alter_post_creation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subcribers',
            field=models.ManyToManyField(related_name='categories', to=settings.AUTH_USER_MODEL),
        ),
    ]
