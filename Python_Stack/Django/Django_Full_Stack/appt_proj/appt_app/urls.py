from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('users/create', views.create_user),
    path('success', views.success),
    path('users/login', views.login),
    path('users/logout', views.logout),	
    path('appointments', views.appointments),
    path('appointments/new', views.new_appointment),
    path('appointments/add_new_appointment', views.add_new_appointment),
    path('appointments/<int:appointment_id>/edit', views.edit_appointment),	   
    path('appointments/<int:appointment_id>/edited_appointment', views.edited_appointment),
    path('appointments/<int:appointment_id>/delete', views.delete),
]