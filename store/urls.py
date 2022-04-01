from django.urls import path

from . import views

urlpatterns = [
	path('order/', views.order, name='order'),
	path('order/<str:treat_id>/', views.order, name='order'),
	path('order/details/<str:pk>/', views.orderDetails, name='details'),
	path('order/confirm/<str:pk>/', views.confirmOrder, name='confirm'),
	path('success/', views.confirmSuccess, name='order-success'),
]