from django.urls import path, include
from rest_framework import routers
from taskmaster import views

router = routers.DefaultRouter()
router.register('tasks',views.TaskMasterViewSet,basename='tasks/')

urlpatterns = [
    path('', include(router.urls)),
]
