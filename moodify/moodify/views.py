# pages/views.py
from django.http import HttpResponse
from django.shortcuts import render

def homePageView(request):
    print("Hello Hactoberfest")
    return render(request,'login.html')
