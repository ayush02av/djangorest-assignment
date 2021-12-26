from django.db import models
from django.utils import timezone
from uuid import uuid4

# Create your models here.
class task(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	createdAt = models.DateTimeField(default=timezone.now)
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)

	def __str__(self):
		return f'{name} - {description} by {email}'