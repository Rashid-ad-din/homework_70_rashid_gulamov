from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


class AddTaskView(TemplateView):
    template_name = 'add_task.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = TaskForm()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        task = request.POST.get('state')
        if form.is_valid():
            task = form.save()
            return redirect('show_task', pk=task.pk)
        return render(request, 'add_task.html', context={'form': form})


class TasksView(TemplateView):
    template_name = 'tasks.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class UpdateView(TemplateView):
    template_name = 'edit_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm(instance=context['task'])
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            return redirect('show_task', pk=task.pk)
        return render(request, 'edit_task.html', context={'form': form})
