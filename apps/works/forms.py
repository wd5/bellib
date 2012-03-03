# -*- coding: utf-8 -*-

from models import Work
from models import Vote
from models import WorkText
from models import WorkAudio
from models import WorkImages
from django import forms

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ('work', 'evaluation')

    def clean(self):
        cd = self.cleaned_data
        if 0.0 > float(cd.get('evaluation', -1.0)) > 5.0:
            raise forms.ValidationError('Недопустимое значение оценки.')
        return cd

class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('name', 'info', 'description', )

class WorkTextForm(forms.ModelForm):
    class Meta:
        model = WorkText
        fields = ('file', )

class WorkAudioForm(forms.ModelForm):
    class Meta:
        model = WorkAudio
        fields = ('file', )

class WorkImagesForm(forms.ModelForm):
    class Meta:
        model = WorkImages
        fields = ('file', )