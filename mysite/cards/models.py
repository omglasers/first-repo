from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Card(models.Model):
	url_field = models.URLField(max_length=200)
	name = models.CharField(max_length=60)
	image = models.ImageField(upload_to='uploads')
	media_type = models.CharField(max_length=32)
	created_at = models.DateTimeField("created at")
	def __str__(self):
		return self.name