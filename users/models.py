from pyexpat import model
from django.contrib import admin
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
	email = models.EmailField(unique=True)
	avatar = models.ImageField(upload_to='avatars/',default='avatar.svg')

	# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	# phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

	phone_number = PhoneNumberField()

	dob = models.DateField(verbose_name='date of birth', null=True, blank=True)

	role = models.ForeignKey('Role', on_delete=models.SET_NULL, default=None, null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']


	def __str__(self):
		return f'{self.first_name} {self.last_name}'


class Role(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name