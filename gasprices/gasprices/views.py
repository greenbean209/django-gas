from email import contentmanager
from multiprocessing import context
from re import template
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('gasprices/index.html')
    context = {'something':'here is something'}
    return HttpResponse(template.render(context))