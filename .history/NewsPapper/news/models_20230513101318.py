from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)


class Category(models.Model):
    name = models.CharField(max_length=64, unique = True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    ARTICLE = 'AR'
    NEWS = 'NW'
    CATEGORY_CHOICES = (
        (ARTICLE, 'Статья'),
        (NEWS, 'Новость')
    )


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    pass
