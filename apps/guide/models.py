# -*- coding: utf-8 -*-

from django.db import models

class Guide(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = models.TextField('Текст')
    show = models.BooleanField('Показывать', default=True)

    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'