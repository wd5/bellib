# -*- coding: utf-8 -*-

from django import forms
from django.contrib.admin.models import User
from django.utils.translation import ugettext_lazy as _

class AuthenticationForm(forms.Form):
    email = forms.EmailField(label=_("Email"), max_length=75)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)

            if user.check_password(password):
                self.user_cache = user
        except User.DoesNotExist:
            raise forms.ValidationError(_("Please enter a correct username and password. Note that both fields are case-sensitive."))

        return self.cleaned_data