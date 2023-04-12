from django.shortcuts import render
import requests
import socket
from proxy.views import proxy_view
from django.http import StreamingHttpResponse

# Create your views here.

def home(request):
    # print("got to home")
    # hostname = socket.gethostname()
    # print(hostname)
    # hostname = socket.gethostbyname(hostname)
    # print(hostname)
    # print(socket.getfqdn())
    # context = {"hostname": hostname}
    return render(request,'streamlit/home.html')
    # response = requests.get("http://127.0.0.1:8501", stream=True)
        
    # return StreamingHttpResponse(
    #     response.raw,
    #     content_type=response.headers.get('content-type'),
    #     status=response.status_code,
    #     reason=response.reason)

def djproxy(request,path):
    remoteurl = "http://127.0.0.1:8501" + path
    return proxy_view(request, remoteurl)

def streamlitproxy(request,resource):
    print(resource)
    if request.method == "GET":
        response = requests.get("http://127.0.0.1:8501/"+resource, stream=True)
        
        return StreamingHttpResponse(
            response.raw,
            content_type=response.headers.get('content-type'),
            status=response.status_code,
            reason=response.reason)
    elif request.method == "POST":
        response = requests.post("http://127.0.0.1:8501/"+resource, request.POST, stream=True)
        #may need to include files, you'd have to do a whole files thing
        
        return StreamingHttpResponse(
            response.raw,
            content_type=response.headers.get('content-type'),
            status=response.status_code,
            reason=response.reason)