from django.shortcuts import render
# import rest_framework.response to rednder data into JSON
from rest_framework.response import Response


# import rest_framework.decorators to specify which methods we want to use in the rest framework
from rest_framework.decorators import api_view
# import Quiz class model
from .models import Quiz
# import serializers
from .serializer import QuizSerializer


@api_view(["GET"])
def base(request):
    return render(request, "base.html", {})

@api_view(["GET"])
def questions(request):
    quizzes = Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    # This will return our data in JSON format 
    
    quiz_1 = {
        'quiz_name' : "what is 1 + 1 ?",
        'quiz_answer' : "option_3",
        'option_1' : "3",
        'option_2' : "4",
        'option_3' : "2",
        'option_4' : "1",
        'score_to_pass' : "50"
    }
    quiz_2 = {
        'quiz_name' : "What are two colors that imply a desire and calm?",
        'quiz_answer' : ["option_1", "option_3"],
        'option_1' : "red",
        'option_2' : "yellow",
        'option_3' : "blue",
        'option_4' : "black",
        'score_to_pass' : "50"
    }
    quiz_lists = [quiz_1, quiz_2]
    print(request)
    return render(request, "base.html", {serializer:serializer})

@api_view(["POST"])
def quiz_answer(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

