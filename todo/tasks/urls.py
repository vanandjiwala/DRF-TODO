from django.contrib import admin
from django.urls import path
from .views import task_list,task_detail, TaskList

urlpatterns = [
    path('tasks/', TaskList.as_view()),
    path('tasks/<int:id>/', task_detail),
]
