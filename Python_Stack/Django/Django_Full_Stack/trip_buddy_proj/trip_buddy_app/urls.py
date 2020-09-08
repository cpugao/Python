from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('users/create', views.create_user),
    path('dashboard', views.dashboard),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('trips/new', views.new_trip),
    path('trips/add_new_trip', views.add_new_trip),
    path('trips/<int:trip_id>', views.view_trip),
    path('trips/edit/<int:trip_id>', views.edit_trip),
    path('trips/edited/<int:trip_id>', views.edited_trip),
    path('trips/<int:trip_id>/delete', views.delete),
]
