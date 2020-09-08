from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('book/<int:book_id>', views.view_book),
    path('book/<int:book_id>/add_author', views.add_author),
    path('author', views.author),
    path('create_author', views.create_author),
    path('author/<int:author_id>', views.view_author),
    path('author/<int:author_id>/add_book', views.add_another_book),
]