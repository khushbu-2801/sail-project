from django.shortcuts import render
from django.http import HttpResponse
from detector.models import *
from detector.forms import *
from django.core.mail import send_mail
from .helpers import forgot_mail
# Create your views here.


def homePage(request):
    send_mail(
        'Testing mail',
        'Here is the message.',
        'sailauthority31@gmail.com',
        ['to@example.com'],
        fail_silently=False,
    )


def login(request):
    return render(request, 'login.html')


def reg(request):
    return render(request, 'reg.html')


def ins(request):
    if request.method == 'POST':
        t = registration()
        t.fname = request.POST.get('fname')
        t.lname = request.POST.get('lname')
        t.uname = request.POST.get('uname')
        t.email = request.POST.get('email')
        t.phone = request.POST.get('phone')
        t.psw = request.POST.get('psw')
        t.save()
        return render(request, 'login.html')
    else:
        return HttpResponse("Error, data are not feeded")


def login_request(request):
    uname = request.POST.get('uname')
    psw = request.POST.get('psw')
    try:
        t = registration.objects.get(uname=uname, psw=psw)
        x = vehicledb.objects.all()
        return render(request, "page.html", {'x': x})
    except:
        return render(request, 'login.html')


def Showdata(request):
    x = vehicledb.objects.all()
    return render(request, 'page.html', {'x': x})


def forgot(request):
    return render(request, 'forgot.html')


def reset(request):
    return render(request, 'reset.html')
