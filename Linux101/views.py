from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
	#return HttpResponse('homepage')
	return render(request,'homepage.html')

# def structured_learning(request):
#	 return render(request, 'structured_learning.html')

def faq(request):
	return render(request, 'faq.html')

def aboutUs(request):
	#return HttpResponse('about')
	return render(request,'about.html')

def contactUs(request):
	return render(request,'contactUs.html')
