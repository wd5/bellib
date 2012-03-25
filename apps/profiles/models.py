# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_delete

from django.contrib.auth.models import User
from publicauth.models import PublicID
from registration.models import RegistrationProfile

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    did_training = models.BooleanField('Прошел разминку', default=False)
    scores = models.FloatField('Кол-во правильных ответов', default=0.0)

def delete_user(instance, **kwargs):
    Profile.objects.filter(user=instance).delete()
    PublicID.objects.filter(user=instance).delete()
    RegistrationProfile.objects.filter(user=instance).delete()
    instance.delete()
post_delete.connect(delete_user, sender=User)