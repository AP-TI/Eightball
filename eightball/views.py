from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
    file = open(r"C:\Users\maxim\Documents\webservices\examen\eightball\eightball.txt")
    eightball = file.readlines()
    answer = eightball[random.randint(0, len(eightball) - 1)]
    return render(request, 'eightball/index.html', {'eightball': answer})