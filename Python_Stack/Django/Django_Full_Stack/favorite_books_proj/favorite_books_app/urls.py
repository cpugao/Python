from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_reg),
    path('users/create', views.create_user),
    path('books', views.books),
    path('users/login', views.login),
    path('users/logout', views.logout),
    path('books', views.books),
    path('books/<int:book_id>', views.view_book),
    path('add_book_form', views.add_book_form),
    path('books/<int:book_id>/add_favorite', views.add_favorite),
    path('books/<int:book_id>/edit', views.edit_book),
    path('books/<int:book_id>/remove_from_favorites', views.remove_from_favorites),
    path('books/<int:book_id>/delete', views.delete)
]