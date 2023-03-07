from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def vaishu(request):
    return HttpResponse('<h1> vaishu is worstfallow</h1>')
def mickey(request):
    return HttpResponse('<h1>mickey is worst fallow</h1>')

