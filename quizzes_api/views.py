from django.shortcuts import render
# import rest_framework.response 
from rest_framework.response import Response
# import rest_framework.decorators to specify which methods we want to use in the rest framework
from rest_framework.decorators import api_view
# import Quiz class model
from quizzes_api.models import Quiz
# import serializers
from quizzes_api.serializer import QuizSerializer


@api_view(["GET"])
def home(request):
    return render(request, "home.html", {})

@api_view(["GET"])
def quizzes(request):
    return render(request, "quizzes.html", {})

# A quiz_list function 
@api_view(["GET"])
def quiz_list(request):
    # a variable that contains a complex data
    quizzes = Quiz.objects.all() 
    # create a list variable
    serializer = QuizSerializer(quizzes, many = True)
    return Response(serializer.data)

@api_view(["POST"])
def quiz_answer(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)