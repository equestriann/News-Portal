from django.forms import Form, CharField, EmailField, IntegerField
from .models import Post


class PostForm(Form):
    email = EmailField()
    text = CharField()
    number = IntegerField()