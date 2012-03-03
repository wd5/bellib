# -*- coding: utf-8 -*-

from django.db import models
from fields import AutoOneToOneField

from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
#    user = AutoOneToOneField(User, primary_key=True)
    user = models.ForeignKey(User, unique=True)
    phone = models.CharField('Телефон', help_text='Контактный телефон автора работ', max_length=32, null=True, blank=True)
    did_training = models.BooleanField('Прошел разминку', default=False)
    scores = models.FloatField('Кол-во правильных ответов', default=0.0)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)