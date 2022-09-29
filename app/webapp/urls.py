from django.urls import path

from webapp.views.base import home_view
from webapp.views.items import item_view, add_view, edit_view, delete_view, items_view, confirm_delete_view

urlpatterns = [
    path('', home_view, name='home'),
    path('items/', items_view, name='show_items'),
    path('items/item/<pk>/', item_view, name='show_item'),
    path('items/item/add/', add_view, name='add_item'),
    path('items/item/<pk>/edit/', edit_view, name='edit_item'),
    path('items/item/<pk>/delete/', delete_view, name='delete_item'),
    path('items/item/<pk>/confirm-delete/', confirm_delete_view, name='confirm_delete_item')
]
