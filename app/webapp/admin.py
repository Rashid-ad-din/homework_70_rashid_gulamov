from django.contrib import admin

from webapp.models import Item

list_display = ('id', 'state', 'desscription', 'date_to_do')
list_filter = ('id', 'state', 'desscription', 'date_to_do')
search_fields = ('state', 'description', 'date_to_do')
fields = ('id', 'state', 'desscription', 'date_to_do')
readonly_fields = ('id', 'date_to_do')

admin.site.register(Item)
