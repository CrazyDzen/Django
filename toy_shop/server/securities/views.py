from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import login, logout
from . import forms


class LoginView(FormView):
    template_name = 'securities/login.html'
    success_url = reverse_lazy('products:list')
    form_class = forms.LoginForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


class RegisterView(FormView):
    template_name = 'securities/register.html'
    success_url = reverse_lazy('products:list')
    form_class = forms.RegisterForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})
