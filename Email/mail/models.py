from django.db import models

# Create your models here.

class emailsystem(models.Model):
	receiver_email=models.CharField(max_length=100)
	subject=models.CharField(max_length=100)
	message=models.TextField(max_length=500)
