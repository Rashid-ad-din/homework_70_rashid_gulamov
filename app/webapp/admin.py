from django.contrib import admin

from webapp.models import Task, Type, State, Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'get_state', 'get_type', 'created_at', 'updated_at')
    list_filter = ('id', 'summary', 'state', 'type')
    search_fields = ('summary', 'state', 'type')
    fields = ('id', 'summary', 'description', 'state', 'type', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')

    def get_state(self, obj):
        return "\n".join([s.name for s in obj.state.all()])

    def get_type(self, obj):
        return "\n".join([t.name for t in obj.type.all()])


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


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('id', 'title', 'description', 'date_start', 'date_end')
    search_fields = ('id', 'title', 'description')
    fields = ('id', 'title', 'description', 'date_start', 'date_end')
    readonly_fields = ('id', )


admin.site.register(Task, TaskAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Project, ProjectAdmin)
