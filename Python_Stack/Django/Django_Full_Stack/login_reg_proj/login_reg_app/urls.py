from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_reg),
    path('users/create', views.create_user),
    path('success', views.success),
    path('users/login', views.login),
    path('users/logout', views.logout),
]