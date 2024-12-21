from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import ContactUs
from . import serializers


class HomePageView(APIView):

    def get(self,request):
        return Response(data={'message':'This is home page Tru.'},status=status.HTTP_200_OK)
    

class ContactUsView(ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer
    


