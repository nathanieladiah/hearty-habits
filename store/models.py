from random import choices
import uuid
from django.db import models

from contact.models import Customer

class Treat(models.Model):
	ANIMALS = (
		("cat", "Cat"),
		("dog", "Dog"),
	)

	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=15, decimal_places=2, default=25.00)
	description = models.TextField()
	animal = models.CharField(max_length=10, choices=ANIMALS, default='dog')

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUSES = (
		('proc', 'Processing'),
		('ready', 'Ready'),
		('del', 'Delivered')
	)
	treat = models.ForeignKey(Treat, on_delete=models.SET_NULL, null=True)
	count = models.IntegerField()
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	confirmed = models.BooleanField(default=False)
	status = models.CharField(max_length=20, choices=STATUSES, default='proc')
	uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
	date_ordered = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.customer.name}'s order of {self.treat}"

	@property
	def total(self):
		return "%.2f" %(float(self.treat.price) * float(self.count))