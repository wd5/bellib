# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

def main_page(request):

    return render_to_response('simple_pages/main_page.html',
    {

    }, context_instance=RequestContext(request))

def login_page(request):

    return render_to_response('simple_pages/login_page.html',
    {

    }, context_instance=RequestContext(request))