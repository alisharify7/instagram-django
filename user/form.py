from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import ValidationError
from django.contrib.auth import get_user_model
from validators.email import email as emailvalidator

User = get_user_model()


class RegisterForm(forms.Form):
    EmailOrPhone = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    EmailOrPhone.widget.attrs.update({'class': 'form-control my-1 fs-0-8', 'placeholder': _('Mobile Number or Email')})

    FullName = forms.CharField(max_length=256, required=True, widget=forms.TextInput())
    FullName.widget.attrs.update({'class': 'form-control my-1 fs-0-8', 'placeholder': _('Full Name')})

    Username = forms.CharField(max_length=154, required=True, widget=forms.TextInput())
    Username.widget.attrs.update({'class': 'form-control my-1 fs-0-8', 'placeholder': _('Username')})

    Password = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput())
    Password.widget.attrs.update({'class': 'form-control my-1 fs-0-8', 'placeholder': _('Password')})

    SubmitText = _('Sing Up')

    def clean_EmailOrPhone(self):
        # just for now check only email
        email = self.cleaned_data["EmailOrPhone"]
        if (user := User.objects.filter(email=email).first()):
            # self.add_error("EmailOrPhone", _("there is already a user registered with this email."))
            raise ValidationError(_('there is already a user registered with this email.'))

        if not emailvalidator(email):
            # self.add_error("EmailOrPhone", _("invalid email address."))
            raise ValidationError(_('invalid email address.'))

        return self.cleaned_data["EmailOrPhone"]

    def clean_Username(self):
        if not self.cleaned_data['Username'].isidentifier():
            # self.add_error("Username", _("Username is invalid."))
            raise ValidationError(_('Username is invalid.'))

        username = self.cleaned_data['Username']
        if (user := User.objects.filter(username=username).first()):
            # self.add_error(_('there is already a user registered with this email.'))
            raise ValidationError(_('there is already a user registered with this username.'))

        return self.cleaned_data["Username"]

    def save(self):
        """save user to db"""
        EmailOrPhone, FullName, Username, Password = self.cleaned_data["EmailOrPhone"], self.cleaned_data["FullName"], \
        self.cleaned_data["Username"], self.cleaned_data["Password"]
        user = User.objects.create_user(username=Username, email=EmailOrPhone, password=Password, fullname=FullName)
        return user


class LoginForm(forms.Form):
    EmailOrPhone = forms.CharField(max_length=254, required=True, widget=forms.TextInput())
    EmailOrPhone.widget.attrs.update(
        {'class': 'form-control my-1 fs-0-8', 'placeholder': _('Phone Number, username or email')})

    Password = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput())
    Password.widget.attrs.update({'class': 'form-control my-1 fs-0-8', 'placeholder': _('Password')})

    SubmitText = _('Log in')

    def save(self):
        """save user to db"""
        EmailOrPhone, FullName, Username, Password = self.cleaned_data["EmailOrPhone"], self.cleaned_data["FullName"], \
        self.cleaned_data["Username"], self.cleaned_data["Password"]
        user = User.objects.create_user(username=Username, email=EmailOrPhone, password=Password)
        return user