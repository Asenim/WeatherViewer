from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
# from django.views import View
from django.contrib.auth import authenticate, login
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

# class UserRegistration(DataMixin, CreateView):
#     form_class = UserRegistrationForm
#     template_name = 'users_templates/user_registration.html'
#     success_url = reverse_lazy('login')
#
#     def get(self, request):
#         context = {
#             'form': UserRegistrationForm()
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = UserRegistrationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             user_name = form.cleaned_data.get('username')
#             user_email = form.cleaned_data.get('email')
#             user_password = form.cleaned_data.get('password1')
#             print(user_name, user_email, user_password)
#
#             return redirect('login')
#
#         context = {
#             'form': form
#         }
#
#         return render(request, self.template_name, context)
