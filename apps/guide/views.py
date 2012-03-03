# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Guide

def guide_list(request):

    return render_to_response('guide/list.html',
    {
        'guides': Guide.objects.filter(show = True),
    }, context_instance=RequestContext(request))