from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.models import Item


def items_view(request: WSGIRequest):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'items.html', context)


def item_view(request: WSGIRequest, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item.html', context={'item': item, 'status': Item.CHOICES})


def add_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_item.html', context={'status': Item.CHOICES})
    date_to_do = None
    if request.POST.get('date_to_do'):
        date_to_do = request.POST.get('date_to_do')
    item_data = {
        'description': request.POST.get('description'),
        'description_details': request.POST.get('description_details'),
        'state': request.POST.get('state'),
        'date_to_do': date_to_do
    }
    item = Item.objects.create(**item_data)
    url = reverse('show_item', kwargs={'pk': item.pk})
    return HttpResponseRedirect(url)


def edit_view(request: WSGIRequest, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'GET':
        date = str(item.date_to_do)
        return render(request, 'edit_item.html', context={'item': item, 'date': date, 'status': Item.CHOICES})
    date_to_do = None
    if request.POST.get('date_to_do'):
        date_to_do = request.POST.get('date_to_do')
    item.description = request.POST.get('description')
    item.description_details = request.POST.get('description_details')
    item.state = request.POST.get('state')
    item.date_to_do = date_to_do
    item.save()
    return redirect('show_item', pk=item.pk)


def delete_view(request: WSGIRequest, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('show_items')
