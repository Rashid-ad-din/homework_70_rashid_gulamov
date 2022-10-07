from django.urls import path

from webapp.views.base import HomeView
from webapp.views.items import item_view, add_view, edit_view, delete_view, items_view, confirm_delete_view
from webapp.views.tasks import TasksView, TaskView, AddTaskView

urlpatterns = [
    path('', TasksView.as_view(), name='show_tasks'),
    path('items/add/', AddTaskView.as_view(), name='add_task'),
    path('items/', TasksView.as_view(), name='show_tasks'),
    path('items/<pk>/', TaskView.as_view(), name='show_task'),
    path('items/<pk>/edit/', edit_view, name='edit_item'),
    path('items/<pk>/delete/', delete_view, name='delete_item'),
    path('items/<pk>/confirm-delete/', confirm_delete_view, name='confirm_delete_item')
]
