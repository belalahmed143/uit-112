from django.urls import path 
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration', registration, name='registration'),
    path('login', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='userapp/logout.html'), name='logout'),
    path('profile', profile, name='profile'),
    path('profile-update', profileUpdate, name='profile-update'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='userapp/password-change.html'), name='password-change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='userapp/password_change_done.html'), name='password_change_done'),
]