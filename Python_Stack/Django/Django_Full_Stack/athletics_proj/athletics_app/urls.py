from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	
    path('users/create', views.create_user),
    path('dashboard', views.dashboard),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('users/<int:user_id>', views.user_profile),
    path('users/<int:user_id>/edit', views.edit_profile),
    path('users/<int:user_id>/edited', views.edited_profile),
    path('users/<int:user_id>/delete', views.delete),
    path('message_board', views.message_board),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('message/<int:message_id>/delete', views.delete_message),
    path('comment/<int:comment_id>/delete', views.delete_comment),
]