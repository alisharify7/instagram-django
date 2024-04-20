from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseNotAllowed
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from .form import RegisterForm, LoginForm

from lib.http_method import get_next_page

#
#
# from django.views.generic import FormView
# class clsRegisterView(FormView):
#     form_class = RegisterForm
#     template_name = "instagram_auth/register.html"
#     success_url = redirect(reverse('instagram_auth:login-view'))
#
#     def form_valid(self, form):
#         form.save() # save changes in db
#         messages.success(self.request, _("successful registration."))
#         return super().form_valid(form)
#

def RegisterView(request):
    ctx = {
        "form": RegisterForm()
    }
    next = get_next_page(request=request) or reverse('auth:login-view')

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            ctx["form"] = form
            messages.warning(request, _("missing value. invalid form"))
            return render(request, "instagram_auth/register.html", context=ctx)

        form.save()
        messages.success(request, _("successful registration."))
        return redirect(next)

    elif request.method == "GET":
        return render(request, "instagram_auth/register.html", context=ctx)
    else:
        return HttpResponseNotAllowed("Method not allowed")

def LoginView(request):
    ctx = {
        "form": LoginForm()
    }

    next = get_next_page(request=request) or reverse('auth:login-view')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if not form.is_valid():
            ctx["form"] = form
            return render(request, "instagram_auth/login.html", context=ctx)

        username = form.cleaned_data["EmailOrPhone"]
        password = form.cleaned_data["Password"]
        user = authenticate(request=request, username=username, password=password)

        if not user:
            messages.warning(request, _("invalid credential! ."))
            return redirect(next)

        login(request=request, user=user)
        messages.success(request, _("welcome back {}".format(user.fullname)))
        return redirect(next)

    elif request.method == "GET":
        return render(request, "instagram_auth/login.html", context=ctx)
    else:
        return HttpResponseNotAllowed("Method not allowed")

