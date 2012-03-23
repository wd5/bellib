# -*- coding: utf-8 -*-

from django.contrib import admin
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from models import Work, Training, CleanRatioRequest

class CleanRatioRequestAdmin(admin.ModelAdmin):
    list_display = ('pub_date', )
    list_filter = ('pub_date', )
    search_fields = ('comment', )

    def save_form(self, request, form, change):
        obj = super(CleanRatioRequestAdmin, self).save_form(request, form, change)

        message = render_to_string('works/cleanratio.html', {'comment': obj.comment, })
        for superuser in User.objects.filter(is_superuser=True):
            superuser.email_user(u'Запрос на очистку рейтинга', message)

        return obj

admin.site.register(CleanRatioRequest, CleanRatioRequestAdmin)
admin.site.register(Work)
admin.site.register(Training)