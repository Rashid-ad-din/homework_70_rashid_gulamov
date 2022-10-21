from django.urls import path

from webapp.views.projects import ProjectsView, ProjectAddView, ProjectView, ProjectUpdateView, ProjectDeleteView
from webapp.views.tasks import TasksView, TaskView, AddTaskView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', TasksView.as_view(), name='show_tasks'),
    path('tasks/add/', AddTaskView.as_view(), name='add_task'),
    path('tasks/', TasksView.as_view(), name='show_tasks'),
    path('tasks/<pk>/', TaskView.as_view(), name='show_task'),
    path('tasks/<pk>/edit/', TaskUpdateView.as_view(), name='edit_task'),
    path('tasks/<pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/<pk>/confirm-delete/', TaskDeleteView.as_view(), name='confirm_delete_task'),

    path('projects/', ProjectsView.as_view(), name='show_projects'),
    path('projects/add/', ProjectAddView.as_view(), name='add_project'),
    path('projects/<pk>/', ProjectView.as_view(), name='show_project'),
    path('projects/<pk>/add-task/', AddTaskView.as_view(), name='add_project_task'),
    path('projects/<pk>/edit/', ProjectUpdateView.as_view(), name='edit_project'),
    path('projects/<pk>/delete/', ProjectDeleteView.as_view(), name='delete_project'),
    path('projects/<pk>/confirm-delete-project/', ProjectDeleteView.as_view(), name='confirm_delete_project')
]
