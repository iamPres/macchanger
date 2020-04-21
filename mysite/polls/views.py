from django.shortcuts import render
from django.http import HttpResponse

import subprocess

def index(request):
    subprocess.call(["sudo","ifconfig","eth0","down"])
    subprocess.call(["sudo","macchanger","--mac","88:71:E5:3A:E5:B5","eth0"])
    subprocess.call(["sudo","ifconfig","eth0","up"])
    return HttpResponse("MAC Address set.")
# Create your views here.
