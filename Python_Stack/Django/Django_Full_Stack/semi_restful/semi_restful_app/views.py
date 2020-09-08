from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Show

def shows(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    
    return render(request, 'shows.html', context)

def new_show(request):

    return render(request, 'add-show.html')

def add_show(request):
    print(request.POST)
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect('/shows/new')

    show = Show.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            release_date = request.POST['release_date'],
            desc = request.POST['desc']
    )

    return redirect(f'/shows/{show.id}')

def created_show(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show' : show
    }

    return render(request, 'created-show.html', context)

def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.release_date = show.release_date.strftime("%Y-%m-%d")
    context = {
        'show' : show
    }

    return render(request, 'edit-show.html', context)

def edited_show(request, show_id):
    show = Show.objects.get(id=show_id)
    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)

        return redirect(f'/shows/{show.id}/edit')

    show.title = request.POST["title"]
    show.network = request.POST["network"]
    show.release_date = request.POST["release_date"]
    show.desc = request.POST["desc"]

    show.save()

    return redirect(f'/shows/{show.id}')

def destroy(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()

    return redirect('/shows')



# Create your views here.
