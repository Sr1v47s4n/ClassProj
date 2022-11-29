from django.urls import path
from . import views

urlpatterns = [
    path("addStudent", views.addStudent.as_view()),
    path("manageStudent", views.manageStudent.as_view()),
]
