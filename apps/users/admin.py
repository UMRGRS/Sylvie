from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Company, CompanyUser
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'company')
    fieldsets = ((None, 
                  {'fields':('username', 'password', 'company')}), ('Permissions',{'fields':('is_superuser', 'is_staff', 'is_active')}),)
    add_fieldsets = ((None, {'classes': ('wide',), 'fields': ('username', 'company', 'password1', 'password2',)}),)
    readonly_fields=('is_staff', 'is_active', 'is_superuser')
    search_fields =('username',)
    ordering = ('username',)
    filter_horizontal = ()
    
admin.site.register(Company)
admin.site.register(CompanyUser, UserAdmin)
admin.site.unregister(Group)