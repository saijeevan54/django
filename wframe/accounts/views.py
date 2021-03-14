from django.contrib.auth import get_user_model
from .utils import get_and_authenticate_user
from . import serializers
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework import viewsets, status
from django.core.exceptions import ImproperlyConfigured
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from accounts.serializers import RoleSerializer, TaskSerializer, Task2Serializer, ProjectSerializer
from django.contrib.auth.models import User
from core.models import Project, Tasks
from tasks.models import Role
from django.core import serializers


class RoleView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        role = Role.objects.all()
        serialized_queryset = serializers.serialize('json', role)
        return serialized_queryset


class UserCreate(APIView):
    """ 
    Creates the user. 
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskCreate(APIView):
    """ 
    Creates the Tasks. 
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            if task:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Task2Create(APIView):
    """ 
    Creates the Tasks. 
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = Task2Serializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            if task:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectCreate(APIView):
    """ 
    Creates the Project. 
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = serializer.save()
            if project:
                print(project)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


User = get_user_model()
