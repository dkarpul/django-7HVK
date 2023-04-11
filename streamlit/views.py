from django.shortcuts import render
import socket

# Create your views here.

def home(request):
    hostname = socket.gethostname()
    context = {"hostname": hostname}
    return render(request,'streamlit/home.html',context)    