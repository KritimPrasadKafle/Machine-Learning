from django.shortcuts import render
# from rest_framework import viewsets
from .models import User
from rest_framework import APIView
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.
class UserAPI(APIView):
    def get(request):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data)


