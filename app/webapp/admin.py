from django.contrib import admin

from app.webapp.models import Item, Task, Type, State


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'description', 'date_to_do')
    list_filter = ('id', 'state', 'description', 'date_to_do')
    search_fields = ('state', 'description', 'date_to_do')
    fields = ('id', 'state', 'description', 'description_details', 'date_to_do')
    readonly_fields = ('id', 'date_to_do')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'state', 'type', 'created_at', 'updated_at')
    list_filter = ('id', 'summary', 'state', 'type')
    search_fields = ('summary', 'state', 'type')
    fields = ('id', 'summary', 'description', 'state', 'type', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id',)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    fields = ('id', 'name')
    readonly_fields = ('id',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Type, TypeAdmin)
