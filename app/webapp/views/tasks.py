import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView

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
        context['tasks'] = Task.objects.filter(state__name__in=('Сделано', 'В процессе'),
                                               type__name__in=('Баг', 'Улучшение'))
        return context

    def post(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        tasks_to_delete = request.POST.getlist('task')
        Task.objects.filter(pk__in=tasks_to_delete).delete()
        context['tasks'] = Task.objects.all()
        return self.render_to_response(context)


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
        return render(request, 'edit_task.html', context={'form': form, 'task': task})


class DeleteView(TemplateView):
    template_name = 'delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ConfirmDeleteView(RedirectView):
    def get(self, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('show_tasks')
