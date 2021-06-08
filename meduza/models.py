from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	lek = models.CharField(max_length=50)
	godzina = models.CharField(max_length=10, null=True)

	def get_absolute_url(self):
		return reverse('meduza-home')
