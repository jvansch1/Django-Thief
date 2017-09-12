# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    template = loader.get_template('todos/index.html')
    context = {
        'todos': todos
    }
    return HttpResponse(template.render(context, request))
