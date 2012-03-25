# -*- coding: utf-8 -*-

import os
from django import template

register = template.Library()

@register.filter
def filename(value):
    try:
        return os.path.basename(value.file.name)
    except IOError:
        return ''