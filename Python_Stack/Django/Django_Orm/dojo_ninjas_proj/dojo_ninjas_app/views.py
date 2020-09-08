from django.shortcuts import render, redirect

from .models import Dojo, Ninja

def index(request):
    context = {
        'all_dojos': Dojo.objects.all()
    }

    return render(request, 'index.html', context)

def add_dojo(request):
    Dojo.objects.create(
        name = request.POST['dojo_name'],
        city = request.POST['city'],
        state = request.POST['state']
    )

    return redirect('/')

def add_ninja(request):
    Ninja.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        dojo_id = Dojo.objects.get(id=request.POST['dojo']),
    )

    return redirect('/')

def delete(request):
    Dojo.objects.get(id=request.POST['dojo']).delete()

    return redirect('/')

# Create your views here.
