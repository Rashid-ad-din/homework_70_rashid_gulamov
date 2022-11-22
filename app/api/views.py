from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializer, TaskSerializer
from webapp.models import Project, Task


class DetailView(APIView):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs['upk'])
        task = get_object_or_404(Task, pk=kwargs['pk'])
        project_serializer = ProjectSerializer(project)
        task_serializer = TaskSerializer(task)
        data = {'project': project_serializer.data, 'task': task_serializer.data}
        return Response(data, status=status.HTTP_200_OK)


class UpdateView(APIView):
    def put(self, request, upk, pk, *args, **kwargs):
        project = get_object_or_404(Project, pk=upk)
        task = get_object_or_404(Task, pk=pk)
        project_serializer = ProjectSerializer(project, data=request.data.get('project'))
        task_serializer = TaskSerializer(task, data=request.data.get('task'))

        if project_serializer.is_valid() & task_serializer.is_valid():
            project_serializer.save()
            task_serializer.save()
            data = {'project': project_serializer.data, 'task': task_serializer.data}
            return Response(data, status=status.HTTP_200_OK)
        else:
            errors = {'project errors': project_serializer.errors, 'task errors': task_serializer.errors}
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteView(APIView):
    def delete(self, request, upk, pk, *args, **kwargs):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        project = get_object_or_404(Project, pk=upk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
