from django.urls import path

from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('profile/<str:pk>/', views.userProfile, name='profile')
]