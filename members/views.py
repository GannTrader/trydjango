from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from django.utils.translation import gettext, gettext_lazy as _

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView


class SiteVerifyUser(TemplateView):
    template_name = "registration/verified_user.html"


class SidebarLoginView(View):
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return redirect("register")



class EditLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username or email...'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Password...'}),
    )

class SiteLoginView(LoginView):
    form_class = EditLoginForm
    template_name = "registration/login.html"


class EditRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email"]

        widgets = {
            "username": forms.TextInput(attrs=({
                "class": "form-control",
                "placeholder": "Username..."
            })),
            "email": forms.TextInput(attrs=({
                "class": "form-control",
                "placeholder": "Email..."
            })),
        }
    def __init__(self, *args, **kwargs):
        super(EditRegisterForm, self).__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({"class": "form-control", "placeholder": "Password..."})
        self.fields["password2"].widget.attrs.update({"class": "form-control", "placeholder": "Confirm password..."})



class SiteRegisterView(CreateView):
    form_class = EditRegisterForm
    model = User
    template_name = "registration/register.html"
    success_url = reverse_lazy("posts")

class SiteLogoutView(LogoutView):
    template_name = "registration/logout.html"


class ProfileView(View):
    template_name = "registration/profile.html"
    def get(self, request):
        user_courses = request.user.groups.all()
        context = {"user_courses": user_courses}
        return render(request, self.template_name, context)


#change password
class SitePasswordChangeView(PasswordChangeView):
    template_name = "passwordmanager/change-password.html"
    success_url = reverse_lazy("login")