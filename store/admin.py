from django.contrib import admin

from .models import Order, Treat

@admin.register(Treat)
class TreatAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'animal')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ('treat', 'customer', 'count', 'confirmed', 'date_ordered')
	readonly_fields = ('date_ordered', )