# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth import authenticate, login

from forms import AuthenticationForm

def login_by_email(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['email'], password = cd['password'])
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET.get('next'))
            else:
                return HttpResponseRedirect('/')

    return render_to_response('registration/login.html',
    {
        'form': form,
    }, context_instance=RequestContext(request))

def facebook_new_user(request):
    print request.GET

    return render_to_response('registration/login.html',
    {

    }, context_instance=RequestContext(request))

@login_required
def facebook_complite(request):

    return render_to_response('registration/login.html',
    {

    }, context_instance=RequestContext(request))