from django.shortcuts import render
from django.http import HttpResponse
import random as rnd
# Create your views here.

def home(request):
    # return HttpResponse('Hello there friends')
    return render(request, 'generator/home.html')

def about_coder(request):
    return render(request, 'generator/about_coder.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    length = int(request.GET.get('length', 12))
    thepassword = ''

    for x in range(length):
        thepassword += rnd.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword })
