from django.shortcuts import render, redirect

from .models import Book, Author

def index(request):
    context = {
        'all_books' : Book.objects.all()
    }

    return render(request, 'index.html', context)

def add_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc']
    )
    return redirect('/')

def view_book(request, book_id):
    context = {
        'this_book' : Book.objects.get(id=book_id),
        'all_authors' : Author.objects.all()
    }

    return render(request, 'view-book.html', context)

def add_author(request, book_id):
    # book_id
    # request.POST["selected_author_id"]
    
    # Grab the book
    # Grab the author
    # Add author to the book's author list
    book = Book.objects.get(id=book_id)
    selected_author = Author.objects.get(id=request.POST["selected_author_id"])
    book.books_written.add(selected_author)

    # return redirect('/book/' + str(book_id))
    return redirect(f'/book/{book_id}')

def author(request):
    context = {
        'all_authors' : Author.objects.all()
    }

    return render(request, 'author.html', context)

def create_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/author')

def view_author(request, author_id):
    context = {
        'this_author' : Author.objects.get(id=author_id),
        'all_books' : Book.objects.all()
    }

    return render(request, 'view-author.html', context)

def add_another_book(request, author_id):
    author = Author.objects.get(id=author_id)
    selected_book = Book.objects.get(id=request.POST['selected_book_id'])
    author.books.add(selected_book)

    return redirect(f'/author/{author_id}')

# Create your views here.
