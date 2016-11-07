from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    return render(request, 'index.html', {})


def logout(request):
    auth_logout(request)
    return redirect('home')
