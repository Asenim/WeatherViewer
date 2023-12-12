from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def user_logout(request):
    logout(request)
    return redirect('index')
