from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
	owner = models.ForeignKey(User, )
	url_field = models.URLField(max_length=200)
	name = models.CharField(max_length=60)
	image = models.ImageField()
	media_type = models.CharField(max_length=32)
	created_at = models.DateTimeField("created at")



	def __str__(self):
		return self.name