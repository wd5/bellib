# -*- coding: utf-8 -*-

from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django import forms
import os

from annoying.functions import get_object_or_None
from annoying.decorators import autostrip

from registration.models import RegistrationProfile
from publicauth.models import PublicID
from profiles.models import Profile
from publicauth import settings


class ExtraForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=30, label="Имя пользователя")
    email = forms.EmailField(label='Email')

    def clean_username(self):
        if get_object_or_None(User, username=self.cleaned_data['username']):
            raise forms.ValidationError(u'Пользователь с таким именем уже существует')
        return self.cleaned_data['username']

    def clean_email(self):
        if get_object_or_None(User, username=self.cleaned_data['email']):
            raise forms.ValidationError(u'Эта почта уже используется')
        return self.cleaned_data['email']

    def save(self, request, identity, provider):
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        user = RegistrationProfile.objects.create_inactive_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=os.urandom(7),
            site=site,
        )

        PublicID.objects.create(user=user, identity=identity, provider=provider)
        Profile.objects.create(user=user)
        return user

ExtraForm = autostrip(ExtraForm)