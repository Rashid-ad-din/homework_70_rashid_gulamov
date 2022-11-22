from django.urls import path

from api.views import DetailView, UpdateView, DeleteView

urlpatterns = [
    path('project/<int:upk>/task/<int:pk>/', DetailView.as_view(), name='api_project'),
    path('project/<int:upk>/task/<int:pk>/update/', UpdateView.as_view(), name='api_update'),
    path('project/<int:upk>/task/<int:pk>/delete/', DeleteView.as_view(), name='api_delete'),
]
