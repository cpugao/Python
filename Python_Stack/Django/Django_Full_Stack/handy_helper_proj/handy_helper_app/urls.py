from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('users/create', views.create_user),
    path('dashboard', views.dashboard),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('jobs/new', views.new_job),
    path('jobs/add_new_job', views.add_new_job),
    path('jobs/<int:job_id>', views.view_job),
    path('jobs/edit/<int:job_id>', views.edit_job),
    path('jobs/edited/<int:job_id>', views.edited_job),
    path('jobs/<int:job_id>/delete', views.delete),
]