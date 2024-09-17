from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Machine(models.Model):
    identifier = models.CharField(_('Machine identifier'), primary_key=True, max_length=16, blank=False, null=False, unique=True)
    machine = models.CharField(_('Machine type'), max_length=40, blank=False, null=False)
    area = models.CharField(_('Machine location'), max_length=40, blank=False, null=False)
    company = models.ForeignKey(('users.Company'), on_delete=models.CASCADE, related_name="machines", null=False, blank=False)
    
    def __str__(self):
        return f'ID: {self.identifier}, Machine: {self.machine}, Area: {self.area}, Company: {self.company}'
    
    class Meta:
        verbose_name = _('Machine')
        verbose_name_plural = _('Machines')
        
class RealtimeData(models.Model):
    pressure = models.FloatField(_('Pressure'), blank=False, null=False, default=0)
    work_time = models.IntegerField(_('Work time'), blank=False, null=False, default=0)
    stop_time = models.IntegerField(_('Stop time'), blank=False, null=False, default=0)
    tank_level = models.FloatField(_('Tank level'), blank=False, null=False, default=0)
    fluid_volume = models.FloatField(_('Fluid CM3'), blank=False, null=False, default=0)
    machine = models.ForeignKey(('Machine'), on_delete=models.CASCADE, related_name='machineRealtimeData', null=False, blank=False)
    
    def __str__(self):
        return f'Machine: {self.machine.identifier} realtime data'
    
    class Meta:
        verbose_name = _('Realtime data')
        verbose_name_plural = _('Realtime data')
        
class DataLogs(models.Model):
    pressure = models.FloatField(_('Pressure'), blank=False, null=False, default=0)
    work_time = models.IntegerField(_('Work time'), blank=False, null=False, default=0)
    stop_time = models.IntegerField(_('Stop time'), blank=False, null=False, default=0)
    tank_level = models.FloatField(_('Tank level'), blank=False, null=False, default=0)
    fluid_volume = models.FloatField(_('Fluid CM3'), blank=False, null=False, default=0)
    time = models.DateTimeField(_('Log date time'), auto_now_add=True)
    machine = models.ForeignKey(('Machine'), on_delete=models.CASCADE, related_name='machineDataLogs', null=False, blank=False)
    
    def __str__(self):
        return f'Machine: {self.machine.identifier}, Date: {timezone.localtime(self.time).strftime('%b %d, %Y, %I:%M %p')}'
    
    class Meta:
        verbose_name = _('Data log')
        verbose_name_plural = _('Data logs')