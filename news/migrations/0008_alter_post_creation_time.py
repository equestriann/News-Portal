# Generated by Django 4.2.6 on 2023-10-26 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
