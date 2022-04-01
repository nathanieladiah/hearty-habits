from django.urls import path

from . import views

urlpatterns = [
	path('', views.contact, name='contact'),
	path('success/', views.successPage, name='success'),
]