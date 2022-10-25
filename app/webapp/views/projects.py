from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from webapp.forms.projects import ProjectForm, ProjectUsersForm
from webapp.models import Project


class GroupPermission(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('show_project', kwargs={'pk': self.object.pk})


class ProjectAddView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'projects/add_project.html'
    form_class = ProjectForm
    model = Project
    groups = ['admin', 'Project Manager']


class ProjectsView(ListView):
    template_name = 'projects/projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectView(DetailView):
    template_name = 'projects/project.html'
    model = Project

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        devs = []
        devss = project.user.all()
        for dev in devss:
            devs.append(dev.username)
        context = {'project': project, 'devs': devs}

        return self.render_to_response(context)


class ProjectUpdateView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'projects/edit_project.html'
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'
    groups = ['admin', 'Project Manager']


class ProjectDeleteView(GroupPermission, DeleteView, LoginRequiredMixin):
    template_name = 'projects/project_delete.html'
    model = Project
    success_url = reverse_lazy('show_tasks')
    groups = ['admin', 'Project Manager']


class ProjectAddUserView(GroupPermission, SuccessDetailUrlMixin, LoginRequiredMixin, UpdateView):
    template_name = 'projects/add_user.html'
    form_class = ProjectUsersForm
    model = Project
    groups = ['admin', 'Project Manager', 'Team Lead']


def user_delete_view(request: WSGIRequest, pk, upk):
    project = get_object_or_404(Project, pk=pk)
    userr = get_object_or_404(User, pk=upk)
    return render(request, 'partial/user_confirm_delete.html', context={'project': project, 'userr': userr})


def user_confirm_delete_view(request: WSGIRequest, pk, upk):
    project = get_object_or_404(Project, pk=pk)
    user = get_object_or_404(User, pk=upk)
    project.user.remove(user)
    return redirect('show_project', pk)
