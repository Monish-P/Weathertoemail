from django.shortcuts import render,HttpResponse
import json
import urllib.request
from .models import User
from email.message import EmailMessage
from django.conf import settings
import ssl
import smtplib
def index(request):
    return render(request,'core/index.html')
def home(request):
    return render(request,'core/home.html')
def details(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    User.objects.create(name=name,email=email)
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=visakhapatnam&appid=1981e011069b0c3d9df7d41cee425929').read()
    list_of_data = json.loads(source)
    kelvin = list_of_data['main']['temp']
    temp =  str(kelvin) + 'k'
    subject = 'Hi '+name+', your live weather notification'
    celcius = int(kelvin-273.15)
    if celcius in range(-10,6):
        emoji = '🥶'
    elif celcius in range(6,17):
        emoji = '🆒'
    elif celcius in range(18,30):
        emoji = '😊'
    elif celcius in range(31,51):
        emoji = '🔥'
    else:
        emoji = '🥵'
    message = 'The temperature in visakhapatnam is '+temp+' '+emoji
    email_from = 'harimanikanta.basava@gmail.com'
    password = 'bacwckmeyvfcqwkv'
    em = EmailMessage()
    em['From'] = email_from
    em['To'] = email
    em['Subject'] = subject
    em.set_content(message)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
        smtp.login(email_from,password)
        smtp.sendmail(email_from,email,em.as_string())
    return HttpResponse('The weather details have been sent, Check your mail! Thank you🤗')
