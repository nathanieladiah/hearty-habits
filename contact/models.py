from django.db import models
from django.core.validators import RegexValidator

class Customer(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

	def __str__(self):
		return self.email