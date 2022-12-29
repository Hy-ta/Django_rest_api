from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # looking at urls.py in the quizzes_api directory
    path("quizzes/", include("quizzes_api.urls")),
]
