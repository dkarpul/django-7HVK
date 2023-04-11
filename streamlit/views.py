from django.shortcuts import render
import socket

# Create your views here.

def home(request):
    hostname = socket.gethostname()
    print(hostname)
    hostname = socket.gethostbyname(hostname)
    print(hostname)
    print(socket.getfqdn())
    context = {"hostname": hostname}
    return render(request,'streamlit/home.html',context)    