from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    print(request.POST)

    request.session['name'] = request.POST.get("name")
    request.session['location'] = request.POST.get("location")
    request.session['language'] = request.POST.get("language")
    request.session['comments'] = request.POST.get("comments")

    return render(request, 'result.html')

# Create your views here.
