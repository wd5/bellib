# -*- coding: utf-8 -*-

from django.contrib import admin

from models import Guide

class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'show', )
    list_filter = ('show', )
    search_fields = ('title', 'content',)
    list_editable = ['show', ]

admin.site.register(Guide, GuideAdmin)