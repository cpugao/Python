from django.shortcuts import render, redirect

import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['history'] = []

    return render(request, 'index.html')

def process_money(request):
    if 'farm' in request.POST:
        found_gold = random.randint(10,20)
        request.session['gold'] += found_gold
    elif 'cave' in request.POST:
        found_gold = random.randint(5,10)
        request.session['gold'] += found_gold
    elif 'house' in request.POST:
        found_gold = random.randint(2,5)
        request.session['gold'] += found_gold
    elif 'casino' in request.POST:
        found_gold = random.randint(-50,50)
        request.session['gold'] += found_gold

    request.session['history'].append(found_gold)

    return redirect('/')

def reset(request):
    request.session.clear()

    return redirect('/')
