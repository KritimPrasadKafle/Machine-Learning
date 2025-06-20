from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework import status
# Create your views here.

class UserAPI(APIView):
    def get(request, self):
        user = User.objects.all()
        userSerializer = UserSerializer(user, many=True)
        print("2")
        print("UserSeri", userSerializer)
        print("User", user)
        return Response(userSerializer.data)
            

    def post(self, request):
        
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        user_id = request.data.get("id")
        user = User.objects.get(id = user_id)


        serializer = UserSerializer(user, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        user_id = request.data.get("id")
        user = User.objects.get(id = user_id)
        user.delete()
        return Response("Deleted Successfully....", status=status.HTTP_200_OK)