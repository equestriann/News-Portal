# Generated by Django 4.2.6 on 2023-10-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
