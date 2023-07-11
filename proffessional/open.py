from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def moreaboutus(request):
    return render(request,'moreaboutus.html')