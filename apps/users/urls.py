from django.urls import path

from knox import views as knox_views

from .views import LoginView, GetCurrentUser, AdminCreateCompany, AdminGetUpdateDeleteCompany, AdminCreateUser, AdminGetUpdateDeleteUser

urlpatterns = [
     # path(r'admin/company/', AdminCreateCompany.as_view(), name='admin_company_register'),
     # path(r'admin/company/<int:pk>/', AdminGetUpdateDeleteCompany.as_view(), name='admin_company_modify'),
     # path(r'admin/user/', AdminCreateUser.as_view(), name='admin_user_register'),
     # path(r'admin/user/<int:pk>/', AdminGetUpdateDeleteUser.as_view(), name='admin_user_register'),
     path(r'user/', GetCurrentUser.as_view(), name='see_user'),
     path(r'login/', LoginView.as_view(), name='knox_login'),
     path(r'logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     path(r'logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]