from rest_framework import serializers
from quizzes_api.models import Quiz

class QuizSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=50)
    question = serializers.CharField(max_length=1000)
    answer1 = serializers.IntegerField()
    answer2 = serializers.IntegerField()

    def create(self, data):
        return Quiz.objects.create(**data)