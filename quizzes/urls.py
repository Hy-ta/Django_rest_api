from django.contrib import admin
from django.urls import include, path
from quizzes_api.views import home, quizzes

urlpatterns = [
    path("", home, name="home.html"),
    path("admin/", admin.site.urls),
    # looking at urls.py in the quizzes_api directory
    path("quiz/",quizzes, name="quizzes.html"),
    path("quizzes/", include("quizzes_api.urls")),
]
 