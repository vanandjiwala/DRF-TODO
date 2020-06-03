from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime

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







    # def get_queryset(self):
    #     """What to do when an incorrect query string is passed"""
    #     status = self.request.query_params.get('status', None)
    #     queryset = TaskMaster.objects.all()
    #     ordering = ('created_at')
    #     #If there is no status in query string then return all records
    #     if status is None:
    #         return queryset
    #     else:
    #         status = status.lower()
    #         print(status)
    #         #If status has true or false value then we will filter the queryset else return all records for invalid string
    #         if status in ['true','false']:
    #             queryset = queryset.filter(completed=(status=='true'))
    #         else:
    #             return queryset


