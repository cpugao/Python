from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User, Book

def index(request):

    return render (request, 'index.html')

def create_user(request):
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:

        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/')

    hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    
    created_user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = hashed_pw
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

def add_book_page(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']), 
    }
    return render(request, 'add-book-page.html', context)

def create_book(request):
    book = Book.objects.create(
        title = request.POST['title'],
        author = request.POST['author'],
        review = request.POST['review'],
        rating = request.POST['rating'],
        uploaded_by = User.objects.get(id=request.session['user_id'])
    )

    return redirect(f'/books/{book.id}')

def created_book(request, book_id):
    context = {
        'book' : Book.objects.get(id=book_id)
    }

    return render(request, 'individual-book-page.html', context)

def user_page(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }

    return render(request, 'user-page.html', context)



# Create your views here.
