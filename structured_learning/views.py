from django.shortcuts import render

# Create your views here.


def structured_learning(request):
	return render(request, 'structured_learning/structured_learning.html')

def w0(request):
	return render(request, 'structured_learning/w0.html');

def w1(request):
	return render(request, 'structured_learning/w1.html');

def w2(request):
	return render(request, 'structured_learning/w2.html');

def w3(request):
	return render(request, 'structured_learning/w3.html');

def w4(request):
	return render(request, 'structured_learning/w4.html');

def w5(request):
	return render(request, 'structured_learning/w5.html');