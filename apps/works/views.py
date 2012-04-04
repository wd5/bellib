# -*- coding: utf-8 -*-

import os
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import  settings
from django.utils import simplejson
from forms import ApplyForm
from forms import WorkForm
from forms import WorkTextForm
from forms import WorkAudioForm
from forms import WorkImagesForm
from forms import VoteForm
from django.forms.formsets import formset_factory
from StringIO import StringIO
from zipfile import ZipFile

from profiles.models import Profile
from models import Work, Training, Vote, WorkAudio, WorkImages, WorkText, Apply

def works_list(request, user_id = None):
    works = Work.objects.order_by('pub_date')
    template_name = 'works/list.html'
    if user_id:
        works = works.filter(user__id = user_id)
        template_name = 'works/by_user.html'

    query = request.GET.get('query')
    if query:
        template_name = 'works/search.html'
        works = works.filter(
            Q(name__icontains = query) |
            Q(info__icontains = query) |
            Q(description__icontains = query))

    return render_to_response(template_name,
    {
        'works': works,
    }, context_instance=RequestContext(request))

def work_inside(request, work_id):
    work = get_object_or_404(Work, id = work_id)

    return render_to_response('works/inside.html',
    {
        'work': work,
        'text_files': WorkText.objects.filter(work=work),
        'audio_file': WorkAudio.objects.filter(work=work),
        'image_file': WorkImages.objects.filter(work=work),
    }, context_instance=RequestContext(request))

def work_download(request, work_id):
    """ Скачать все файлы работ. """
    work = get_object_or_404(Work, id = work_id)

    in_memory = StringIO()
    zip = ZipFile(in_memory, "a")

    def zip_pack(model, work_id, zip):
        for f in model.objects.filter(work__id = work_id):
            file_name = os.path.join(settings.MEDIA_ROOT, f.file.name)
            zip.write(file_name, arcname=f.file.name)

    zip_pack(WorkText, work_id, zip)
    zip_pack(WorkAudio, work_id, zip)
    zip_pack(WorkImages, work_id, zip)

    for file in zip.filelist: file.create_system = 0
    zip.close()

    response = HttpResponse(mimetype="application/zip")
    response["Content-Disposition"] = "attachment; filename=work_%s.zip" % work.id

    in_memory.seek(0)
    response.write(in_memory.read())

    return response

def works_ratio(request):
    """
    Таблица с рейтингом работ.
    """
    works = []
    for work in Work.objects.all():
        works.append({
            'work': work,
            'ratio': work.get_ratio(),
        })
    works_sorted = sorted(works, key = lambda w: w.get('ratio'), reverse = True) # Сортировка по рейтингу
    works = []
    for work in works_sorted:
        works.append(work['work'])

    return render_to_response('works/ratio.html',
    {
        'works': works,
    }, context_instance=RequestContext(request))

@login_required
def work_add(request, work_id = None):
    work_instance = None
    if work_id:
        work_instance = get_object_or_404(Work, id=work_id)
        work_form = WorkForm(instance=work_instance)
    else:
        work_form = WorkForm()
    TextsFormSet = formset_factory(WorkTextForm, extra=10, max_num=10)
    AudiosFormSet = formset_factory(WorkAudioForm, extra=10, max_num=10)
    ImagesFormSet = formset_factory(WorkImagesForm, extra=10, max_num=10)

    texts_formset = TextsFormSet(prefix='text')
    audios_formset = AudiosFormSet(prefix='audio')
    images_formset = ImagesFormSet(prefix='image')

    if request.method == 'POST':
        work_form = WorkForm(request.POST)
        texts_formset = TextsFormSet(request.POST, request.FILES, prefix='text')
        audios_formset = AudiosFormSet(request.POST, request.FILES, prefix='audio')
        images_formset = ImagesFormSet(request.POST, request.FILES, prefix='image')

        if work_form.is_valid() and \
            texts_formset.is_valid() and audios_formset.is_valid() and images_formset.is_valid():

            if work_id:
                work = get_object_or_404(Work, id = work_id, user = request.user)

                cd = work_form.cleaned_data
                work.name = cd['name']
                work.info = cd['info']
                work.description = cd['description']
                work.save()
            else:
                work = work_form.save(commit=False)
                work.user = request.user
                work.save()

            def save_forms(formset, work):
                for form in formset.forms:
                    if form.is_valid():
                        if form.cleaned_data.get('file', None):
                            file = form.save(commit=False)
                            file.work = work
                            file.save()
            save_forms(texts_formset, work)
            save_forms(audios_formset, work)
            save_forms(images_formset, work)
            return redirect('works_by_user', request.user.id)

    return render_to_response('works/add_work.html',
    {
        'form': work_form,
        'work_instance': work_instance,
        'texts_form_set': texts_formset,
        'audios_form_set': audios_formset,
        'images_form_set': images_formset,
    }, context_instance=RequestContext(request))

@login_required
def work_training(request):
    not_right = 0 # Кол-во неправильных
    if request.user.is_authenticated and request.method == 'POST':
        answerds = {} # Ответы пользователя
        questions = [] # номера вопросов, на которые отвечал пользователь
        for value in request.POST:
            if 'question_id' in value:
                question_id = value.replace('question_id', '')
                questions.append(question_id)
                answerds[int(question_id)] = request.POST[value]

        for q in Training.objects.filter(id__in = questions):
            if answerds[int(q.id)] != str(q.right):
                not_right += 1

        # Сохраняем результаты теста в профиль
        profile = Profile.objects.get(user = request.user)
        profile.did_training = True
        profile.right_answerds = (10 - not_right) * 0.1
        profile.save()

    return render_to_response('works/training.html',
    {
        'not_right': not_right,
        'questions': Training.objects.filter(show=True).order_by('?')[:10],
    }, context_instance=RequestContext(request))

def work_set_evaluation(request):
    """ Проставление оценки проекту. """
    rsponse = {'result': 'success', }
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            is_vate = False # Уже голосовал
            if not isinstance(request.user, AnonymousUser):
                try:
                    Vote.objects.get(work = form.instance.work, user = request.user)
                    is_vate = True
                    rsponse['result'] = 'already_voted'
                except Vote.DoesNotExist:
                    pass
            votes_of_ip = Vote.objects.filter(work = form.instance.work, ip = request.META.get('REMOTE_ADDR', None)).count()
            if votes_of_ip >= settings.VOTE_IP_LIMITED:
                is_vate = True
                rsponse['result'] = 'limited_ip'

            if not is_vate:
                new_vote = form.save(commit=False)
                if not isinstance(request.user, AnonymousUser):
                    new_vote.user = request.user
                new_vote.ip = request.META.get('REMOTE_ADDR', None)
                new_vote.save()

            rsponse['star_ratio'] = form.instance.work.get_star_ratio()

    return HttpResponse(simplejson.dumps(rsponse), mimetype='application/json')

@login_required
def work_apply(request):
    """
    Подать заявку.
    """
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            apply = Apply(user = request.user)
            apply.save()
            return HttpResponseRedirect(reverse('main_page'))

    return render_to_response("works/apply.html",
    {
        'form': form,
    }, context_instance=RequestContext(request))