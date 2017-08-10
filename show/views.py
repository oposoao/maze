# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse
from django.template import RequestContext
from models import Record

def index(request):
        return render_to_response('index.html')
  
def add(request, seconds):
  record = Record(seconds=seconds)
  record.save()
  return redirect("/show")
  
def show(request):
  records = Record.objects.all().order_by("-id")
  return render_to_response('show.html',{'records':records}, context_instance=RequestContext(request))