from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Task
from .serializers import TaskSerializer

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


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


###############OPTIMIZED VIEW WITH DRF APIS ###########################################

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