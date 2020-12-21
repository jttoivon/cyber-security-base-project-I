# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#from . import signals

import logging

from .models import Tag, Entry

log = logging.getLogger("notes")

@login_required
def index(request):
    log.info("Creating the index page")
    entries = Entry.objects.filter(owner=request.user)
    tags = Tag.objects.all()
    template = loader.get_template('notes/index.html')
    context = {
        'entries': entries,
        'tags': tags,
    }
    return HttpResponse(template.render(context,request))

@login_required
def tag(request, tag):
    entries = Entry.objects.filter(tag__tag=tag)
    template = loader.get_template('notes/tag.html')
    context = {
        'entries': entries,
        'tag': tag,
    }
    return HttpResponse(template.render(context,request))

@login_required
def entry(request, id):
    try:
        action = request.POST['action']
        if action == "delete":
            e=Entry.objects.get(pk=id)
            e.delete()
            return HttpResponseRedirect("/notes/")
    except (KeyError):
        pass
    
    context = {'id' : id }
    try:
        e = Entry.objects.get(pk=id)
        context['e']=e
    except ObjectDoesNotExist:
        pass
    template = loader.get_template('notes/entry.html')

    return HttpResponse(template.render(context,request))

@login_required
def add(request):
#    entries = Entry.objects.filter(tags__tag__exact=tag)
    template = loader.get_template('notes/add.html')
    tags = Tag.objects.all()
    context = {
#        'entries': entries,
        'tags': tags,
    }
    return HttpResponse(template.render(context,request))

@login_required
def add2(request):
    try:
        subject = request.POST['subject']
        content = request.POST['content']
    except (KeyError):
        # Redisplay the question voting form.
        tags = Tag.objects.all()
        return render(request, 'notes/add.html', {
            'tags' : tags,
            'error_message': "You did not provide both subject and content.",
        })
    else:
        # Check the input
        if subject == "" or content == "":
            tags = Tag.objects.all()
            return render(request, 'notes/add.html', {
                'tags' : tags,
                'error_message': "You did not provide both subject and content.",
            }) 
        tags = request.POST.getlist('tag')

        # Create model instances
        e = Entry(owner=request.user, subject=subject, content=content, pub_date=timezone.now())
        e.save()
        if tags:
            for tag in tags:
                try:
                    t=Tag.objects.get(tag=tag)
                    e.tag.add(t)
                except Tag.DoesNotExist:
                    e.tag.create(tag=tag)
        e.save()

        #return HttpResponseRedirect("/notes/entry/%i" % e.id)
        return redirect('notes:entry', id=e.id)
