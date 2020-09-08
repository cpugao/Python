from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),	 
    path('users/create', views.create_user),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('books', views.books),
    path('books/add', views.add_book_page),
    path('books/create', views.create_book),
    path('books/<int:book_id>', views.created_book),
    path('users/<int:user_id>', views.user_page)
]