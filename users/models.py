from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Company(models.Model):
    name = models.CharField(_('Company name'), max_length=100, unique=True, blank=False, null= False)
    email = models.EmailField(_('Contact email'), unique=True, blank=False, null=False)
    phone = PhoneNumberField(_('Contact phone'), blank=False, null=False)
    #Remember to change to cloud solution
    logo = models.ImageField(_('Company logo'), blank=True, null=True, upload_to='company_photos')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, company_fk):
        if username is None:
            raise ValueError('Users must have a username')
        user = self.model(username=username, company=company_fk)
        user.set_password(password)
        return user
        
    def create_standard_user(self, username, password, company_fk):
        user = self.create_user(username=username, password=password, company_fk=company_fk)
        user.save()
        return user
    
    def create_superuser(self, username, password):
        user = self.create_user(username=username, password=password, company_fk=None)
        user.is_active, user.is_staff, user.is_superuser = True, True, True
        user.save()
        return user
    
class CompanyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Username'), db_index=True, max_length=20, unique=True, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    company = models.ForeignKey(('Company'), on_delete=models.CASCADE, related_name="companyUser", null=True, blank=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')