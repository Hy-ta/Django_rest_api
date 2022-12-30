from django.urls import path
#import quiz_list function from views
from quizzes_api.views import quiz_list, quiz_answer

urlpatterns = [
    path('list/', quiz_answer),
    path('list/', quiz_list), #return quiz_list data in the url param

]
