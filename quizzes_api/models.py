from django.db import models

# Create a Quiz model
class Quiz(models.Model):
    # Quiz class attributes
    title = models.CharField(max_length=50)
    question = models.CharField(max_length=1000)
    answer1 = models.IntegerField()
    answer2 = models.IntegerField()
    # initialization
    def __str__(self):
        return self.title