from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse("hi there i am ali gharekhani i gonna to learn django this is my hello world!!!")
    return render(request,"about.html")

def home(request):
    # return HttpResponse("this is my home page ")
    return render(request,"home.html")
