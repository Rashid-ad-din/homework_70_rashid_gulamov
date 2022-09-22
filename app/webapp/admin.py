from django.contrib import admin

from webapp.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'description', 'date_to_do')
    list_filter = ('id', 'state', 'description', 'date_to_do')
    search_fields = ('state', 'description', 'date_to_do')
    fields = ('id', 'state', 'description', 'description_details', 'date_to_do')
    readonly_fields = ('id', 'date_to_do')


admin.site.register(Item, ItemAdmin)
