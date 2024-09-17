from django.contrib import admin
from .models import Machine, RealtimeData, DataLogs
# Register your models here.

class DataLogsAdmin(admin.ModelAdmin):
    readonly_fields = ('time', )
    
class MachinesAdmin(admin.ModelAdmin):
    readonly_fields = ('identifier', )

admin.site.register(Machine, MachinesAdmin)
admin.site.register(RealtimeData)
admin.site.register(DataLogs, DataLogsAdmin)