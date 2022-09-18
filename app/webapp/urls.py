from django.urls import path

from webapp.views.base import home_view
from webapp.views.items import item_view, add_view, edit_view, delete_view, items_view

urlpatterns = [
    path('', home_view, name='home'),
    path('items/', items_view, name='items'),
    path('items/item/', item_view, name='item'),
    path('items/item/add/', add_view, name='add'),
    path('items/item/edit/', edit_view, name='edit'),
    path('items/item/delete/', delete_view, name='delete')
]
