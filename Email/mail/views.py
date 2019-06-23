from django.shortcuts import render
from .models import emailsystem
from .serializer import emailModelserializer
from rest_framework.viewsets import ModelViewSet
from .email1 import sendMail
from rest_framework.response import Response
# Create your views here.


class emailsystemViewSets(ModelViewSet):
	model=emailsystem
	serializer_class=emailModelserializer
	permission_classes=()
	queryset=emailsystem.objects.all()


	def get_queryset(self):
		if 'receiver_email' in self.request.GET:
			return emailsystem.objects.filter(receiver_email=self.request.GET['receiver_email'])
		else:
			return emailsystem.objects.all()



	def create(self,request):
		if request.method == "POST":
			emailsystem.objects.create(**request.data)
			sendMail(request.data["receiver_email"],request.data["subject"],request.data["message"])
		return Response("message sended")

