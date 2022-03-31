from django.db import models

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