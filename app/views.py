from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *


# Create your views here.
def insert_topic(request):
    TF=Topicforms()
    d1={'form':TF}
    if request.method=='POST':
        form_data=Topicforms(request.POST)
        if form_data.is_valid():
            form_data.save()
        return HttpResponse('inserted')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WF=Webpageforms()
    d={'form':WF}
    if request.method=='POST':
        form_data2=Webpageforms(request.POST)
        if form_data2.is_valid():
            form_data2.save()
        return HttpResponse('inserted')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    AF=AccessRecordforms()
    d2={'form2':AF}
    if request.method=='POST':
        form_data=AccessRecordforms(request.POST)
        if form_data.is_valid():
            form_data.save()
        return HttpResponse('inserted')
    return render(request,'insert_access.html',d2)