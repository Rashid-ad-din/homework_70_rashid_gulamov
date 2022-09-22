from django.urls import path

from webapp.views.base import home_view
from webapp.views.items import item_view, add_view, edit_view, delete_view, items_view

urlpatterns = [
    path('', home_view, name='home'),
    path('items/', items_view, name='show_items'),
    path('items/item/<pk>', item_view, name='show_item'),
    path('items/item/add/', add_view, name='add_item'),
    path('items/item/edit/<pk>', edit_view, name='edit_item'),
    path('items/item/delete/<pk>', delete_view, name='delete_item')
]
