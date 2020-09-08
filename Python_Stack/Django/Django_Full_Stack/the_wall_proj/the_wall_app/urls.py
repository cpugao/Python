from django.urls import path     
from . import views

urlpatterns = [
    path('', views.login_reg),
    path('users/create', views.create_user),
    path('wall', views.wall),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('post_message', views.post_message),
    path('post_comment', views.post_comment),
    path('comment/<int:comment_id>/delete', views.delete_comment),
]