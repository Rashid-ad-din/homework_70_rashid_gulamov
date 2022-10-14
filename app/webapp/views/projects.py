from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from webapp.forms.projects import ProjectForm
from webapp.models import Project, Task


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('show_project', kwargs={'pk': self.object.pk})


class ProjectAddView(SuccessDetailUrlMixin, CreateView):
    template_name = 'projects/add_project.html'
    form_class = ProjectForm
    model = Project


class ProjectsView(ListView):
    template_name = 'projects/projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectView(DetailView):
    template_name = 'projects/project.html'
    model = Project


class ProjectUpdateView(SuccessDetailUrlMixin, UpdateView):
    template_name = 'projects/edit_project.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'


class ProjectDeleteView(DeleteView):
    template_name = 'projects/project_delete.html'
    model = Project
    success_url = reverse_lazy('show_tasks')
