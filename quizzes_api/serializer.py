from rest_framework import serializers
from quizzes_api.models import Quiz

# We vreate model serializers because the response object cannot nativelyhandle
# complex data types such as Django model instanes
# We'll create serializers for our Quiz model and they will do convert instances of our Quizzes from objects into 
# data types the response objects can understand.


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

# virtualenv .ps

# source bin/activate
# pip install utmp

# python -m pip install Django
# pip3 install djangorestframework
# python manage.py runserver

# /Users/hyuga/newproject/quiz/quizzes