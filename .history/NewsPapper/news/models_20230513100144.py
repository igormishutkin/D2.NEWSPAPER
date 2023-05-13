from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    pass


class Post(models.Model):
    pass


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    pass
