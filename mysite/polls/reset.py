from django.shortcuts import render
from django.http import HttpResponse
import time
import subprocess

def index(request):
    subprocess.call(["sudo","ifconfig","eth0","down"])
    subprocess.call(["sudo","macchanger","--mac","88:71:E5:3A:E5:B5","eth0"])
    subprocess.call(["sudo","ifconfig","eth0","up"])
    time.sleep(10)
    subprocess.call(["sudo","ifconfig","eth0","down"])
    subprocess.call(["sudo","macchanger","-r","eth0"])
    subprocess.call(["sudo","ifconfig","eth0","up"])
    return HttpResponse("MAC Address reset.")
# Create your views here.
