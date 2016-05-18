from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers
from .models import Answer, Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    model = Question
    fields = ('url', 'answer', 'owner', 'created', 'title', 'description')



class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    model = Answer
    fields = ('url', 'owner', 'created', 'text', 'score')
