from django.shortcuts import render, redirect

import random

def index(request):
    if 'randInt' not in request.session:
        request.session['randInt'] = random.randint(1, 100)

        request.session['clue'] =  'Guess'

    return render(request, 'index.html')

def play(request):
    if request.session['randInt'] < int(request.POST['number']):
        request.session['clue'] = 'Too high!'
    elif request.session['randInt'] > int(request.POST['number']):
        request.session['clue'] = 'Too low!'
    else:
        request.session['clue'] = 'Correct!'

    return redirect('/')

# Create your views here.
