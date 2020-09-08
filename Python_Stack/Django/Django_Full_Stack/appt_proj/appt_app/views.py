from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User, Appointment

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

    return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view that page.')

        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['user_id']),
    }

    return render(request, 'success.html', context)

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


    return redirect('/success')

def logout(request):
    request.session.clear()

    return redirect('/')

def appointments(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view that page.')

        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'all_appointments' : Appointment.objects.all(),
    }

    return render(request, 'appointments.html', context)

def new_appointment(request):
    context = {
        'user' : User.objects.get(id=request.session['user_id']), 
    }
    return render(request, 'new-appointment.html', context)

def add_new_appointment(request):
    errors = Appointment.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/appointments/new')
 
    appointment = Appointment.objects.create(
        task = request.POST['task'],
        date = request.POST['date'],
        status = request.POST['status'],
        user = User.objects.get(id=request.session['user_id'])
    )
    

    return redirect('/appointments')

def edit_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.date = appointment.date.strftime("%Y-%m-%d")

    context = {
        'appointment': appointment
    }

    return render(request, 'edit-appointment.html', context)

def edited_appointment(request, appointment_id):
    user = User.objects.get(id=request.session['user_id'])
    appointment = Appointment.objects.get(id=appointment_id)

    errors = Appointment.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect(f'/appointments/{appointment.id}/edit')
    
    appointment.task = request.POST['task']
    appointment.date = request.POST['date']
    appointment.status = request.POST['status']

    appointment.save()

    return redirect('/appointments')

def delete(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()

    return redirect('/appointments')

# Create your views here.


