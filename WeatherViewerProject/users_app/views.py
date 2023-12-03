from django.shortcuts import render


# Create your views here.
def user_authorization(request):
    return render(request, 'users_templates/users_authorization.html')


def user_registration(request):
    return render(request, 'users_templates/user_registration.html')
