from django.db import models

class Navbar(models.Model):
	url = models.CharField(max_length=20)
	title = models.CharField(max_length=20)
	order = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['order']