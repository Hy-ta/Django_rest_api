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
    quiz_1 = Quiz(quiz_list = 1, title = "what is 1 + 1 ?", score_to_pass = 50)
    quiz_1.save()
    # quiz_lists = [quiz_1, quiz_2]
    print(request)
    return render(request, "base.html", {quiz_1})

@api_view(["POST"])
def quiz_answer(request):
    serializer = QuizSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

