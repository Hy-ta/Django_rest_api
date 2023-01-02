from django.db import models
from unittest.mock import Mock

# Create a Quiz model
class Quiz(models.Model):
    # Quiz class attributes
    quiz_list = models.CharField(max_length=30) #max_length required.
    title = models.CharField(max_length=30)
    score_to_pass = models.DecimalField(default=0, decimal_places=2, max_digits=100, help_text="required score in %")

    # return Quiz string models representations
    def __str__(self):
        return f" question list: {self.quiz_list}, question title: {self.title}, score to pass: {self.score_to_pass}"
    def save(self, *args, **kwargs):
        pass

    def test_quiz_model(self):
        quiz_mock = Mock(spec=Quiz)
        quiz_mock.quiz_list = []
        quiz_mock.title = ""
        quiz_mock.score_to_pass = 100
        
        # self.assertEqual(expected, actual)
        self.assertEqual(quiz_mock.quiz_list, "actual")
        self.assertEqual(quiz_mock.title, "actual")
        self.assertEqual(quiz_mock.score_to_pass, "actual")
        quiz_mock.save.assert_called_once()
    

