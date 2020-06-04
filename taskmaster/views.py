from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from django.utils import timezone

from taskmaster import serializers
from taskmaster.models import TaskMaster

class TaskMasterViewSet(viewsets.ModelViewSet):
    """Taskmaster viewset returns all tasks ordered by created date"""
    serializer_class = serializers.TaskMasterSerializer
    queryset = TaskMaster.objects.all().order_by('created_at')


    def list(self, request):
        """override list method to deal with query params"""
        task_status = request.query_params.get('status', None)
        if task_status is None:
            queryset = TaskMaster.objects.all().order_by('created_at')
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            task_status = task_status.lower()
            if task_status in ['true', 'false']:
                queryset = TaskMaster.objects.all().order_by('created_at')
                queryset = queryset.filter(completed=(task_status == 'true')).order_by('created_at')
                serializer = self.serializer_class(queryset,many=True)
                return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)


    def create(self, request, *args, **kwargs):
        """
        I overrode this method to handle the case when a user is creating the task as well as marking it complete at the same time.
        So this method will set completed_at when user is compliting the task while creating it.
        Issue: completed_at value set prior to created_at as I am setting value and then creating the record in DB.
        """
        print(request.data.get('completed'))
        print(type(request.data.get('completed')))
        print(type(False))
        print(request.data.get('completed') == 'False')
        if (request.data.get('completed') is None) or (request.data.get('completed').lower() == 'false'):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer.save(completed_at=timezone.now()))
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def update(self, request, *args, **kwargs):
        """
        In update, there is one field completed_at which needs to be update when user marks task as completed.
        I overrode update method from UpdateModelMixin to change the default behavior.
        When we alter the task, update with check if completed is marked as true or not.
        If completed is marked as true then at that time, completed_at will be set with the method timezone.now()
         which is available in django.utils.
        If completed is reverted back(Task not done) or changes are made, in that case completed_at is maked as null
        """
        instance = self.get_object()
        if request.data.get('completed') is not None:
            print('if')
            task_completed = request.data.get("completed") == 'true'
            instance.completed = task_completed
            instance.completed_at = timezone.now()
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)
        else:
            print('else')
            instance.completed_at = None
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data)


