from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets  # permissions
from .models import Question, Answer
from .serializers import QuestionSerializer, UserSerializer, AnswerSerializer
import requests


def index(request):
    question_list = Question.objects.all()
    context = {'questions': question_list}
    return render(request, 'index.html', context)

def question(request, question_id):
    user = request.user
    question = Question.objects.get(id=question_id)
    answers_list = Answer.objects.filter(question_id=question_id)
    context = {'question': question, 'question_id': question_id,
    'answers_list': answers_list, 'user': user}
    return render(request, 'question.html', context)

def user_question(request):
    return render(request, 'user_questions.html')





class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-created')
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('-score')
    serializer_class = AnswerSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
