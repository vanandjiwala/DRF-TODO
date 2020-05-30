from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Task
from .serializers import TaskSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly
from django.http import Http404
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework import permissions

# @csrf_exempt
# def task_list(request):
#     if request.method == 'GET':
#         snippets = Task.objects.all()
#         serializer = TaskSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def task_detail(request, id):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         desired_task = Task.objects.get(id=id)
#     except Task.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = TaskSerializer(desired_task)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(desired_task, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         desired_task.delete()
#         return HttpResponse(status=204)


###############OPTIMIZED VIEW WITH DRF APIS - Method based ###########################################

#OBSOLETE
@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'GET':
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        task = TaskSerializer(data=data)
        if task.is_valid():
            task.save()
            return Response(task.data, status=status.HTTP_201_CREATED)
        return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

#OBSOLETE
@api_view(['GET','PUT','DELETE'])
def task_detail(request, id):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        desired_task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(desired_task)
        return Response(serializer.data) #200 is default so no need to explicitly use it

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(desired_task, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        desired_task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###############OPTIMIZED VIEW WITH DRF APIS - Class based ###########################################

# class TaskList(APIView):
#
#     def get(self,request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#         data = JSONParser().parse(request)
#         task = TaskSerializer(data=data)
#         if task.is_valid():
#             task.save()
#             return Response(task.data, status=status.HTTP_201_CREATED)
#         return Response(task.errors, status=status.HTTP_400_BAD_REQUEST)

# class TaskDetail(APIView):
#     def get_task(self,id):
#         try:
#             return Task.objects.get(id=id)
#         except Task.DoesNotExist:
#             raise Http404
#
#     def get(self,request,id):
#         desired_task = self.get_task(id)
#         serializer = TaskSerializer(desired_task)
#         return Response(serializer.data)
#
#     def put(self,request,id):
#         desired_task = self.get_task(id)
#         data = JSONParser().parse(request)
#         serializer = TaskSerializer(desired_task, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self,request,id):
#         desired_task = self.get_task(id)
#         desired_task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#MIXINs review but not implemented
###############OPTIMIZED VIEW WITH DRF APIS - Generic class based ###########################################

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer