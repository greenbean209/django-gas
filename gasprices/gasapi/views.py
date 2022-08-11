from django.shortcuts import render
from django.http import HttpResponse

from .gasprices_reader import get_gasprices_html

# Create your views here.
def index(request):
    return HttpResponse("Gas Prices API")

def houston(request):
    response = get_gasprices_html()
    return HttpResponse(response, content_type="text/HTML")