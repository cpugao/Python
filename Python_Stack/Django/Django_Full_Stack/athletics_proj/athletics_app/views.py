from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User, Lift, Message, Comment

def index(request):

    return render(request, 'index.html')

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
        gym = request.POST['gym'],
        email = request.POST['email'],
        password = hashed_pw,
    )

    request.session['user_id'] = created_user.id

    return redirect('/dashboard')

def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view that page.')

        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'all_users' : User.objects.all()
    }

    return render(request, 'dashboard.html', context)

def login(request):
    potential_users = User.objects.filter(email=request.POST['email'])

    if len(potential_users) == 0:
        print('email does not exist')
        messages.error(request, 'Please check your email and password.')

        return redirect('/')

    if not bcrypt.checkpw(
        request.POST['password'].encode(), potential_users[0].password.encode()
    ):
        messages.error(request, 'Please check your email and password.')

        return redirect('/')

    request.session['user_id'] = potential_users[0].id


    return redirect('/dashboard')

def logout(request):

    request.session.clear()

    return redirect('/')

def user_profile(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id),
    }
    
    return render(request, 'user-profile.html', context)

def edit_profile(request, user_id):
    context = {
        'user' : User.objects.get(id=request.session['user_id'])
    }
    
    return render(request, 'edit-user.html', context)

def edited_profile(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.gym = request.POST['gym']
    user.email = request.POST['email']

    user.save()

    return redirect(f'/users/{user.id}')

def delete(request, user_id):
    user = User.objects.get(id=request.session['user_id'])
    user.delete()

    return redirect('/')

def message_board(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'all_messages' : Message.objects.all()
    }

    return render(request, 'message-board.html', context)

def post_message(request):
    user = User.objects.get(id=request.session['user_id'])
    Message.objects.create(
        message = request.POST['message'],
        author = user
    )

    return redirect("/message_board")

def post_comment(request):
    user= User.objects.get(id=request.session['user_id'])
    Comment.objects.create(
        comment = request.POST['comment'],
        author = user,
        message = Message.objects.get(id=request.POST['message_id'])
    )

    return redirect('/message_board')

def delete_message(requeest, message_id):
    Message.objects.get(id=message_id).delete()

    return redirect('/message_board')

def delete_comment(rquest, comment_id):
    Comment.objects.get(id=comment_id).delete()

    return redirect('/message_board')



# Create your views here.
