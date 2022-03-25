from django.shortcuts import render, redirect
from django.contrib.auth import logout as log_out
from django.contrib.auth.mixins import LoginRequiredMixin
from user.models import User
from user.forms import LoginForm, RegisterForm
from django.views.generic import ListView, FormView
from django.urls import reverse

class UsersView(ListView):
    paginate_by = 2
    model = User
    template_name = "users.html"


class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm

    def get_success_url(self) -> str:
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        return reverse("all_list")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class LoginView(FormView):
    template_name = "user_login.html"
    form_class = LoginForm

    def get_success_url(self) -> str:
        next_url = self.request.GET.get("next")
        if next_url is not None:
            return next_url
        return reverse("catalog")

    def form_valid(self, form):
        form.auth(self.request)
        return super().form_valid(self.request)

def logout(request):
    log_out(request)
    return redirect("catalog")



    
