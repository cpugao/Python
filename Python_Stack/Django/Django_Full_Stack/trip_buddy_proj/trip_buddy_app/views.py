from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User, Trip


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
        'all_trips' : Trip.objects.all(),
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

def new_trip(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']), 
    }
    return render(request, 'new-trip.html', context)

def add_new_trip(request):
    errors = Trip.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/trips/new')
 
    Trip.objects.create(
        destination = request.POST['destination'],
        start_date = request.POST['start_date'],
        end_date = request.POST['end_date'],
        plan = request.POST['plan'],
        tourist = User.objects.get(id=request.session['user_id'])
    )

    return redirect('/dashboard')

def view_trip(request, trip_id):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'trip' : Trip.objects.get(id=trip_id)
    }

    return render(request, 'view-trip.html', context)

def edit_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.start_date = trip.start_date.strftime("%Y-%m-%d")
    trip.end_date = trip.end_date.strftime("%Y-%m-%d")

    context = {
        'trip': trip
    }

    return render(request, 'edit-trip.html', context)

def edited_trip(request, trip_id):
    user = User.objects.get(id=request.session['user_id'])
    trip = Trip.objects.get(id=trip_id)

    errors = Trip.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect(f'/trips/edit/{trip.id}')
    
    trip.destination = request.POST['destination']
    trip.start_date = request.POST['start_date']
    trip.end_date = request.POST['end_date']
    trip.plan = request.POST['plan']

    trip.save()

    return redirect('/dashboard')

def delete(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    trip.delete()

    return redirect('/')

# Create your views here.
