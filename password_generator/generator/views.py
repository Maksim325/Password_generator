from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def generate_password(length=8):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def home(response):
    try:
        password_length = response.POST['length']
    except:
        password_length = 8
        password = generate_password(int(password_length))
        return render(response, 'generator/home.html' ,context={'password':password})
    password_length = response.POST['length']

    print(response.POST)
    if password_length == '' :
        password_length = 8
    password = generate_password(int(password_length))
    return render(response, 'generator/home.html' ,context={'password':password})
def about(response):
    return render(response,'generator/about.html')
