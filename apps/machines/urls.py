from django.urls import path

from .views import AdminCreateMachine, AdminGetUpdateDeleteMachine, GetMachine, UpdateMachine, DeleteMachine, GetDataLogs

urlpatterns = [
    # path(r'admin/machine/', AdminCreateMachine.as_view(), name='admin_create_machine'),
    # path(r'admin/machine/<int:pk>/', AdminGetUpdateDeleteMachine.as_view(), name='admin_update_machine'),
    path(r'machine/<int:pk>/', GetMachine.as_view(), name='get_machine'),
    path(r'c-admin/machine/<int:pk>/', UpdateMachine.as_view(), name='c_admin_update_machine'),
    path(r'c-admin/machine/<int:pk>/', DeleteMachine.as_view(), name='c_admin_delete_machine'),
    path(r'machine/logs/<int:pk>/', GetDataLogs.as_view(), name='get_data_logs_machine'),
]
