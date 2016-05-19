from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Answer, Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Question
        fields = ('url', 'owner', 'created', 'title', 'description')


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Answer
        fields = ('url', 'owner', 'created', 'text', 'score', 'question')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # questions = serializers.PrimaryKeyRelatedField(
    #         many=True, queryset=Question.objects.all())
    # answers = serializers.PrimaryKeyRelatedField(
    #         many=True, queryset=Answer.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'questions', 'answers')
