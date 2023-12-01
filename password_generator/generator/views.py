from django.shortcuts import render
from django.http import HttpResponse
import random

def home(response):
    return HttpResponse(random.randint(11111111, 99999999))
