# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_delete

from django.contrib.auth.models import User
from registration.models import RegistrationProfile
from apps.works.models import Apply
from annoying.functions import get_object_or_None
from django.dispatch.dispatcher import receiver
from social_auth.signals import pre_update

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    did_training = models.BooleanField('Прошел разминку', default=False)
    scores = models.FloatField('Кол-во правильных ответов', default=0.0)

    @property
    def get_apply_exists(self):
        """
        Подавал ли пользователь заявку.
        """
        if get_object_or_None(Apply ,user=self.user):
            return True
        return False

    @property
    def get_apply_access(self):
        """
        Получил ли пользователь одобрение.
        """
        apply = get_object_or_None(Apply ,user=self.user)
        if not apply:
            return False
        return apply.access

def delete_user(instance, **kwargs):
    Profile.objects.filter(user=instance).delete()
    RegistrationProfile.objects.filter(user=instance).delete()
#    UserSocialAuth.objects.filter(user=instance)
    instance.delete()
post_delete.connect(delete_user, sender=User)

@receiver(pre_update)
def update_person_details(sender, **kwargs):
    if sender.name == 'vkontakte':
        details = kwargs.get('details')
        user = kwargs.get('user')
        user.username = details['first_name'] + '_' + details['lastname']
        user.save()

    return True
