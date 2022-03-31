from django.urls import path

from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('profile/<str:pk>/', views.userProfile, name='profile'),

	path('users/', views.userList, name='user-list'),
	path('users/create/', views.createUser, name='create-user'),
	path('users/update/<str:pk>/', views.updateUser, name='update-user'),
]