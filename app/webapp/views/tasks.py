import datetime
from urllib.parse import urlencode

from django.db.models import Q, F

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView

from webapp.forms import TaskForm
from webapp.forms.tasks import SearchForm
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


class TasksView(ListView):
    template_name = 'tasks.html'
    model = Task
    context_object_name = 'tasks'
    ordering = ('created_at',)
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')
        return None

    def get_queryset(self):
        queryset = super().get_queryset().all()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            print(query.__dict__)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
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
