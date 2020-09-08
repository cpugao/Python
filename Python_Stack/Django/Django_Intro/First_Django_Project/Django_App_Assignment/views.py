from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

def root(request):
    return HttpResponse("This is from the root method.")

def index(request):
    return HttpResponse("This is from the index method.")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog: {number}")

def destroy(request, number):
    return redirect("/blogs")

# Create your views here.
