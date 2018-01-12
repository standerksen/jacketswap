from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegisterForm, LoginForm


class RegisterFormView(View):
    form_class = RegisterForm
    template_name = 'user/registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.username = username
            user.set_password(password)

            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        # Form not valid/user not authenticated/user not active
        return render(request, self.template_name, {'form': form})


class LoginFormView(View):
    form_class = LoginForm
    template_name = 'user/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

        # Form not valid/user not authenticated/user not active
        return render(request, self.template_name, {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')
