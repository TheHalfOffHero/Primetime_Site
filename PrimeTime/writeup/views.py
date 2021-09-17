from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def writeup_view(request):
    return HttpResponse('<h1>This is a test</h1>')