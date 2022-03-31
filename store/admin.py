from django.contrib import admin

from .models import Treat

@admin.register(Treat)
class TreatAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'animal')