from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.

def article_list(request):
	# all the articles stored in data base are taken into the articles variable
	# data is the filed by which we want to order our articles
	articles = Article.objects.all().order_by('date')  
	return render(request, 'articles/article_list.html', {'articles':articles})

def article_detail(request,slug):
	#return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request, 'articles/article_detail.html',{'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST,request.FILES) # this is validating the data we recieved on request.POST
		if form.is_valid():
			#save article to db
			instance = form.save(commit = False) #commit will be saved in a next step
			instance.author = request.user  #got the instance and saved the author to it according to the user
			instance.save()			# and now we will commit the instance
			return redirect('articles:list')
	else:	
		form = forms.CreateArticle()
	return render(request,'articles/article_create.html', {'form':form})