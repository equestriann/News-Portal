# Generated by Django 4.2.6 on 2023-11-01 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_category_subcribers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name': 'Промежуточная модель PostCategory', 'verbose_name_plural': 'Промежуточная модель PostCategories'},
        ),
    ]
