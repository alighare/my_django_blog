
from django.shortcuts import render,HttpResponse,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles=models.Articles.objects.all().order_by("-date")
    args={"articles":articles}
    return render(request,"articles/article_list.html",args)
def articles_details(request,slug):
    # return HttpResponse(slug)
    articles=models.Articles.objects.get(slug=slug)
    args={"articles":articles}
    return render(request,"articles/article_details.html",args)

@login_required(login_url="/user_accounts/login")
def create_article(request):
    if request.method=="POST":
        form=forms.CreateArticles(request.POST,request.FILES)
        if form.is_valid:
            #save forms
            temp=form.save(commit=False)
            temp.author=request.user
            temp.save()
            return redirect('articles:list')
    else:
        form=forms.CreateArticles()
    return render(request,"articles/create_article.html",{'form':form})
