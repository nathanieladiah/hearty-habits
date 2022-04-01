from django.contrib import admin

from .models import Navbar

# Register your models here.
@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
	list_display = ('title', 'url', 'order')