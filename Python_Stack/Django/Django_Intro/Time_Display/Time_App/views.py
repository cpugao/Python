from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "time": strftime("%b %d, %Y %H:%M %p", gmtime())
    }
    return render(request, 'index.html', context)
# Create your views here.
