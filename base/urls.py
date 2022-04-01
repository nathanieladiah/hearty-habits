from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('treats/', views.treats, name='treats'),
	path('grooming/', views.grooming, name='grooming'),
]