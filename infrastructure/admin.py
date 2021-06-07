from django.contrib import admin
from . import models
from django.contrib import admin
from django.contrib.admin.models import LogEntry



# Logentry is registrated and set to readonly
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



#logentry and corpora are registered in admin
admin.site.register(LogEntry,LogEntryAdmin)
admin.site.register(models.corpora)

