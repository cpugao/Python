from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User, Book

def login_reg(request):
    
    return render(request, 'login.html')

def create_user(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        print('we have errors')

        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/')

    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    
    created_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw,
    )

    request.session['user_id'] = created_user.id

    return redirect('/books')


def login(request):
    #check if email in db
    potential_users = User.objects.filter(email=request.POST['email'])

    if len(potential_users) == 0:
        print('email does not exist')
        messages.error(request, 'Please check your email and password.')

        return redirect('/')

    #check if password matches

    if not bcrypt.checkpw(
        request.POST['password'].encode(), potential_users[0].password.encode()
    ):
        messages.error(request, 'Please check your email and password.')

        return redirect('/')

    request.session['user_id'] = potential_users[0].id


    return redirect('/books')

def logout(request):
    request.session.clear()

    return redirect('/')

def books(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view that page.')

        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'all_books' : Book.objects.all()
    }

    return render(request, 'books.html', context)

def add_favorite(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects. get(id=book_id)
    user.liked_books.add(book)
    user.save()

    return redirect(f'/books/{book_id}')


def add_book_form(request):
    errors = Book.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key , val in all_errors.items():
            messages.error(request, val)
        return redirect('/books')

    book = Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        uploaded_by = User.objects.get(id=request.session['user_id'])
    )

    return redirect(f'/books/{book.id}')

def view_book(request, book_id):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'book' : Book.objects.get(id=book_id)
    }
    return render(request, 'individual-book.html', context)

def edit_book(request, book_id):
    errors = Book.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key , val in all_errors.items():
            messages.error(request, val)
        return redirect('f/books/{book.id}')

    book = Book.objects.get(id=book_id)

    book.title = request.POST['title']
    book.desc = request.POST['desc']
    book.save()

    return redirect('/books')

def remove_from_favorites(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    user.liked_books.remove(book)
    user.save()

    return redirect (f'/books/{book_id}')

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()

    return redirect('/books')




    




# Create your views here.
