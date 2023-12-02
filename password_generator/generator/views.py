from django.shortcuts import render
from django.http import HttpResponse
import random

def home(response):
    print(response.POST)
    return render(response, 'generator/home.html' ,context={'password':random.randint(11111111, 99999999)})
