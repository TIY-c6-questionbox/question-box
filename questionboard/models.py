from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    owner = models.ForeignKey('auth.User', default='')
    created = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='')
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ('score', )


class Question(models.Model):
    answer = models.ForeignKey('Answer', default=1)
    owner = models.ForeignKey('auth.User', default=1)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=True, default='')
    description = models.TextField(default='')

    class Meta:
        ordering = ('created', )
