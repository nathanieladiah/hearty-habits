from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()
from .models import Role
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ('email', 'first_name', 'last_name', 'role')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
	pass