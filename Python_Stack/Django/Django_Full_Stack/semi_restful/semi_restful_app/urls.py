from django.urls import path

from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.new_show),
    path('shows/create', views.add_show),
    path('shows/<int:show_id>', views.created_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/edited', views.edited_show),
    path('shows/<int:show_id>/destroy', views.destroy)
]