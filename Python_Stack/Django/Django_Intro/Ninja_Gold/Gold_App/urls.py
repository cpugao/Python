from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('findgold', views.process_money),
    path('reset', views.reset),
]