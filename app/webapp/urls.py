from django.urls import path

from webapp.views.tasks import TasksView, TaskView, AddTaskView, UpdateView, DeleteView, ConfirmDeleteView

urlpatterns = [
    path('', TasksView.as_view(), name='show_tasks'),
    path('items/add/', AddTaskView.as_view(), name='add_task'),
    path('items/', TasksView.as_view(), name='show_tasks'),
    path('items/<pk>/', TaskView.as_view(), name='show_task'),
    path('items/<pk>/edit/', UpdateView.as_view(), name='edit_task'),
    path('items/<pk>/delete/', DeleteView.as_view(), name='delete_task'),
    path('items/<pk>/confirm-delete/', ConfirmDeleteView.as_view(permanent=True), name='confirm_delete_task')
]
