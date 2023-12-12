from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# from django.views import View
from django.contrib.auth import authenticate, login, logout
from users_app.forms import UserLoginForm, UserRegistrationForm
#from django.views.generic import CreateView
#from rest_framework.reverse import reverse_lazy


# Create your views here.
def user_authorization(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }
    return render(request, 'users_templates/users_authorization.html', context)


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user_authorization'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'users_templates/user_registration.html', context)
