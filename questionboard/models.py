# from django.contrib.auth.models import User
from django.db import models


class Answer(models.Model):
    owner = models.ForeignKey('auth.User', default='')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ('score', )


class Question(models.Model):
    owner = models.ForeignKey('auth.User', default=1)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(default='')

    class Meta:
        ordering = ('created', )


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     score = models.IntegerField(default=0)
