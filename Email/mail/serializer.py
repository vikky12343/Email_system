from rest_framework import serializers
from .models import emailsystem

class emailModelserializer(serializers.ModelSerializer):
	class Meta:
		model=emailsystem
		fields='__all__'