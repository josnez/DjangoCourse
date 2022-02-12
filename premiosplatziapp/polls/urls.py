from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  #Exam: /polls/5/
  path("<int:question_id>/", views.index, name="index"),
  #Exam: /polls/5/results
  path("<int:question_id/results>/", views.index, name="index"),
  #Exam: /polls/5/vote
  path("<int:question_id/vote>/", views.index, name="index"),
]