from django.urls import path
from . import views


urlpatterns = [
    path("", views.questions),
    path("submit/", views.quiz_answer),
    path("quiz/",views.base, name="base.html"),
]
