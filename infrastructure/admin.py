from django.contrib import admin
from . import models
from django.contrib import admin
from django.contrib.admin.models import LogEntry

# Register your models here.
class LogEntryAdmin(admin.ModelAdmin):
    readonly_fields = ('content_type',
        'user',
        'action_time',
        'object_id',
        'object_repr',
        'action_flag',
        'change_message'
    )

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(LogEntry,LogEntryAdmin)
admin.site.register(models.corpora)

