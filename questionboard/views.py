from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .models import Question, Answer
from .serializers import QuestionSerializer, UserSerializer, AnswerSerializer



def index(requests):
    pass


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-created')
    serializer_class = QuestinoSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-score')
    serializer_class = AnswerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
