from django.shortcuts import render
from .models import Video, Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.

def index(request):
    video = Video.objects.all()
    return render (request, 'video/index.html', {"video":video})


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': 'task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response (serializer.data)


@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response (serializer.data)


@api_view(['POST'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response()

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk) :
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk) :
    task = Task.objects.get(id=pk)
    task.delete()
    return Response ()