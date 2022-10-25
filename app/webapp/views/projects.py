from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from webapp.forms.projects import ProjectForm, ProjectUsersForm
from webapp.models import Project


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('show_project', kwargs={'pk': self.object.pk})


class ProjectAddView(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
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


class ProjectUpdateView(SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'projects/edit_project.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'


class ProjectDeleteView(DeleteView, LoginRequiredMixin):
    template_name = 'projects/project_delete.html'
    model = Project
    success_url = reverse_lazy('show_tasks')


class ProjectAddUserView(SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'projects/add_user.html'
    form_class = ProjectUsersForm
    model = Project


def user_delete_view(request: WSGIRequest, pk, upk):
    project = get_object_or_404(Project, pk=pk)
    userr = get_object_or_404(User, pk=upk)
    return render(request, 'partial/user_confirm_delete.html', context={'project': project, 'userr': userr})


def user_confirm_delete_view(request: WSGIRequest, pk, upk):
    project = get_object_or_404(Project, pk=pk)
    user = get_object_or_404(User, pk=upk)
    project.user.remove(user)
    return redirect('show_project', pk)
