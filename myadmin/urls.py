from django.urls import path

from . import views

urlpatterns = [
	path('', views.dashboard, name='dashboard'),
	path('profile/<str:pk>/', views.userProfile, name='profile'),

	path('users/', views.userList, name='user-list'),
	path('users/create/', views.createUser, name='create-user'),
	path('users/update/<str:pk>/', views.updateUser, name='update-user'),
	path('users/delete/<str:pk>/', views.deleteUser, name='delete-user'),

	path('treats/', views.treats_list, name='treat-list'),
	path('treats/create/', views.addNewTreat, name='create-treat'),
	path('treats/update/<str:pk>/', views.updateTreat, name='update-treat'),
	path('treats/delete/<str:pk>/', views.deleteTreat, name='delete-treat'),
]