from django.urls import path

from knox import views as knox_views

from .views import LoginView, AdminCreateCompany, AdminGetUpdateDeleteCompany, AdminCreateUser, AdminUpdateDeleteUser, GetUser

urlpatterns = [
     # path(r'company/', AdminCreateCompany.as_view(), name='Admin_company_register'),
     # path(r'company/<int:pk>/', AdminGetUpdateDeleteCompany.as_view(), name='Admin_company_modify'),
     # path(r'user/', AdminCreateUser.as_view(), name='Admin_user_register'),
     # path(r'user/<int:pk>/', AdminUpdateDeleteUser.as_view(), name='Admin_user_register'),
     path(r'user/<int:pk>/', GetUser.as_view(), name='Admin_user_register'),
     path(r'login/', LoginView.as_view(), name='knox_login'),
     path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]