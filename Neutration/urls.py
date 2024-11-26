from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout_view,name='logout'),
    path('Admin',views.admin_view,name='Admin'),
    path('dashboard',views.dashboard_view,name='Adashboard'),
    path('udashboard',views.udashboard_view,name='udashboard'),
]