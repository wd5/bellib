# -*- coding: utf-8 -*-

from grappelli.dashboard import modules, Dashboard
from django.conf import settings

class CustomIndexDashboard(Dashboard):
    def __init__(self, **kwargs):
        super(CustomIndexDashboard, self).__init__(**kwargs)
        self.columns = 2

    def init_with_context(self, context):
        if settings.DEBUG:
            self.children.append(modules.AppList(
                title='Applications',
                column=2,
                collapsible=True,
                exclude=('django.contrib.*',),
            ))
        else:
            self.children.append(modules.RecentActions(
                title='Последние действия',
                column=3,
                collapsible=False,
                limit=15,
            ))

        self.children.append(modules.AppList(
            title='Работы пользователей',
            collapsible=True,
            column=1,
            models=(
                'apps.works.models.Work',
                'apps.works.models.Training',
                'apps.works.models.Apply',
            ),
        ))
        self.children.append(modules.AppList(
            title='Оформление сайта',
            column=1,
            collapsible=True,
            models=(
                'flatpages.*',
                'treemenus.*',
                'guide.*',
            ),
        ))

        request = context['request']
        if request.user.is_superuser:
            self.children.append(modules.AppList(
                title='Администрирование',
                collapsible=True,
                column=1,
                models=(
                    'django.contrib.*',
                    'publicauth.*',
                )
            ))