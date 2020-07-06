
from django.shortcuts import render,HttpResponse
from . import models

def article_list(request):
    articles=models.Articles.objects.all()
    args={"articles":articles}
    return render(request,"articles/article_list.html",args)
def articles_details(request,slug):
    # return HttpResponse(slug)
    articles=models.Articles.objects.get(slug=slug)
    args={"articles":articles}
    return render(request,"articles/article_details.html",args)
