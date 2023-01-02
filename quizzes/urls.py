from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path("", base, name="base.html"),
    path("", include("quizzes_api.urls")),
    path("admin/", admin.site.urls),
    # looking at urls.py in the quizzes_api directory
]
 
 