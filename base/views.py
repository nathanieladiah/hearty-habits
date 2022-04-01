from django.shortcuts import render

from store.models import Treat

def home(request):
	return render(request, 'base/home.html')

def about(request):
	return render(request, 'base/about.html')

def treats(request):
	treats = Treat.objects.all()
	return render(request, 'base/treats.html', {'treats': treats})

def grooming(request):
	return render(request, 'base/grooming.html')