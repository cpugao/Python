from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt

from .models import User, Job

def index(request):

    return render(request, 'index.html')


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

    return redirect('/dashboard')


def dashboard(request):
    if 'user_id' not in request.session:
        messages.error(request, 'You must be logged in to view that page.')

        return redirect('/')

    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'all_jobs' : Job.objects.all(),
    }

    return render(request, 'dashboard.html', context)


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


    return redirect('/dashboard')


def logout(request):
    request.session.clear()

    return redirect('/')


def view_job(request, job_id):
    user = User.objects.get(id=request.session['user_id'])
    job = Job.objects.get(id=job_id)

    return render(request, 'view-job.html')


def edit_job(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        'job': job
    }

    return render(request, 'edit-job.html', context)


def edited_job(request, job_id):
    errors = Job.objects.basic_validator(request.POST)

    if len(errors) > 0:

        for key, val in errors.items():
            messages.error(request, val)

        return redirect(f'/jobs/edit/{job.id}')

    user = User.objects.get(id=request.session['user_id'])
    job = Job.objects.get(id=job_id)

    job.title = request.POST['title']
    job.desc = request.POST['desc']
    job.location = request.POST['location']

    job.save()

    return redirect('/dashboard')


def new_job(request):
    user = User.objects.get(id=request.session['user_id'])

    return render(request, 'new-job.html')


def add_new_job(request):
    errors = Job.objects.basic_validator(request.POST)

    if len(errors) > 0:

        for key, val in errors.items():
            messages.error(request, val)

        return redirect('jobs/new')
 
    job = Job.objects.create(
        title = request.POST['title'],
        desc = request.POST['desc'],
        location = request.POST['location'],
        helper = User.objects.get(id=request.session['user_id'])
    )

    return redirect('/dashboard')

def view_job(request, job_id):
    context = {
        'user' : User.objects.get(id=request.session['user_id']),
        'job' : Job.objects.get(id=job_id)
    }

    return render(request, 'view-job.html', context)

def delete(request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()

    return redirect('/dashboard')






# Create your views here.
