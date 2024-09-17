from django.contrib import admin
from .models import Machine, RealtimeData, DataLogs
# Register your models here.

class DataLogsAdmin(admin.ModelAdmin):
    readonly_fields = ('time', )

admin.site.register(Machine)
admin.site.register(RealtimeData)
admin.site.register(DataLogs, DataLogsAdmin)