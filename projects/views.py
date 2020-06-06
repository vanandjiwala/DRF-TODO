from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from projects import serializers
from .models import Project

class ProjectViewSet(viewsets.ModelViewSet):
    """Taskmaster viewset returns all tasks ordered by created date"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProjectSearializer
    queryset = Project.objects.all()