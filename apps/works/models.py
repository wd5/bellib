# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from fields import ContentTypeRestrictedFileField
from django.db import models

class Work(models.Model):
    _EVALUATIONS = (
        (0, 'Неудовлетворительное'),
        (1, 'Хорошее'),
        (2, 'Отличное'),
    )
    user = models.ForeignKey(User, verbose_name='Пользователь')
    name = models.CharField('Название работы', max_length=32)
    evaluation_quality = models.IntegerField('Оценка библиотекарем', choices=_EVALUATIONS, blank=True, null=True)
    info = models.CharField('Краткое описание', max_length=128)
    description = models.TextField('Подробное описание работы', blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def get_ratio(self):
        """ Рейтинг работы """
        votes = [vote.evaluation for vote in Vote.objects.filter(work = self)]
        votes_count = len(votes)
        ratio_people = sum(votes)

        # Оценка "службы качества" библиотекаря + за ответ на вопросы
        ratio_quality = 0
        if self.evaluation_quality:
            if self.evaluation_quality == 1: ratio_quality = 0.5
            if self.evaluation_quality == 2: ratio_quality = 1.0
        ratio_quality = 0.5 * self.user.get_profile().scores + 0.1 * (ratio_quality + 1)
        if ratio_quality > 0.7: ratio_quality = 0.7 # Не должна превышать 0.7

        return ratio_people -\
                (ratio_people - ratio_quality) /\
                (votes_count + 1)**(votes_count * 0.02 / (ratio_people + 0.1))

    def get_voting_user(self):
        """ Кол-во проголосовавщих """
        return Vote.objects.filter(work = self).count()

    def get_star_ratio(self):
        ratio = self.get_ratio()
        star_ratio = {'ratio': ratio, }
        if not ratio: star_ratio['width'] = 25 # 1 звёзда
        if 0.00 < ratio <= 0.25: star_ratio['width'] = 50
        if 0.25 < ratio <= 0.50: star_ratio['width'] = 75
        if 0.50 < ratio <= 0.75: star_ratio['width'] = 100
        if 0.75 < ratio <= 1.00: star_ratio['width'] = 125 # 5 звёзд
        return star_ratio

    def has_files(self):
        if WorkText.objects.filter(work = self).count(): return True
        if WorkAudio.objects.filter(work = self).count(): return True
        if WorkImages.objects.filter(work = self).count(): return True
        return False

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

class Training(models.Model):
    question = models.TextField('Вопрос')
    answerd1 = models.CharField('Ответ #1', max_length=255)
    answerd2 = models.CharField('Ответ #2', max_length=255)
    answerd3 = models.CharField('Ответ #3', max_length=255)
    answerd4 = models.CharField('Ответ #4', max_length=255)
    right = models.IntegerField('Номер правильного ответа', choices=[(i, str(i)) for i in range(1, 5)])
    show = models.BooleanField('Показывать', default=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы к разминке'

class Vote(models.Model):
    work = models.ForeignKey(Work, verbose_name='Работа')
    evaluation = models.FloatField('Оценка')
    pub_date = models.DateTimeField('Оценена', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', blank=True, null=True)
    ip = models.IPAddressField('IP', blank=True, null=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Рейтинг'

class WorkFile(models.Model):
    work = models.ForeignKey(Work, verbose_name='Работа')
    pub_date = models.DateTimeField('Загружен', auto_now_add=True)

class WorkImages(WorkFile):
    file = ContentTypeRestrictedFileField(
        upload_to='work_images',
        max_upload_size=5242880,
        content_types=['image/gif', 'image/jpeg', 'image/png', ]
    )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения работ'

class WorkText(WorkFile):
    file = ContentTypeRestrictedFileField(
        upload_to='work_texts',
        max_upload_size=2621440,
        content_types=[
            'application/octet-stream',
            'rtf',
            'pdf',
            'x-pdf',
            'msword',
            'text/plain',
            'application/pdf',
            'application/msword',
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        ]
    )

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты работ'

class WorkAudio(WorkFile):
    file = ContentTypeRestrictedFileField(
        upload_to='work_audios',
        max_upload_size=10485760,
        content_types=[
            'x-wav',
            'audio/mp4',
            'audio/ogg',
            'audio/mpeg',
            'audio/x-ms-wma',
        ]
    )

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио записи работ'

class CleanRatioRequest(models.Model):
    """
    Запрос на очистку рейтинга.
    """
    comment = models.TextField('Коментарий')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запрос на очистку рейтинга'

class Apply(models.Model):
    """
    Заявка на участие в проекте.
    """
    user = models.OneToOneField(User, verbose_name='Пользователь')
    access = models.BooleanField('Разрешить')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки на участие в проекте'