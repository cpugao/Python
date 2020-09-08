from django.shortcuts import render, redirect

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0

    request.session['count'] = request.session['count'] + 1
    return render(request, 'index.html')

def destroy(request):
    request.session.clear()

    return redirect('/')

# Create your views here.
