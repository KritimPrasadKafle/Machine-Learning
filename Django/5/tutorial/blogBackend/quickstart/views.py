from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, ProfileSerializer, UserWithProfileSerializer, GroupSerializer, PostSerializer
from .models import User, Profile, Group, Post
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your views here.

class UserAPI(APIView):
    def get(self, request):
        print("1")
        user = User.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        print("2")
        result_page = paginator.paginate_queryset(user, request)
        serializer = UserSerializer(result_page, many = True)
        print("3")
        print("Check",serializer)
        return paginator.get_paginated_response(serializer.data)
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)    
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        user_id = request.data.get("id")
        user = User.objects.get(id = user_id)
        print(user_id)
        print(user)
        # if user.DoesNotExist:
        #     return Response("User Doesn't exists", status=status.HTTP_400_BAD_REQUEST)
        user.delete()
        return Response("Deleted Successfully", status=status.HTTP_201_CREATED)

        
class ProfileAPI(APIView):
    def get(self, request):
        profile = Profile.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(profile, request)
        serializer = ProfileSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        profile_id = request.data.get("id")
        try:
            profile = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        profile_id = request.data.get("id")
        try:
            profile = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        profile.delete()
        return Response({"message": "Profile deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class UserWithProfile(APIView):
    def get(self, request,  id): 
        print("11") 
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserWithProfileSerializer(user)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    



class PostAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        try:
            post = Post.objects.get(id=request.data['id'])
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)

        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        try:
            post = Post.objects.get(id=request.data['id'])
            post.delete()
            return Response({"message": "Deleted"}, status=204)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=404)


# ---- Group CRUD ----
class GroupAPI(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request):
        try:
            group = Group.objects.get(id=request.data['id'])
        except Group.DoesNotExist:
            return Response({"error": "Group not found"}, status=404)

        serializer = GroupSerializer(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request):
        try:
            group = Group.objects.get(id=request.data['id'])
            group.delete()
            return Response({"message": "Deleted"}, status=204)
        except Group.DoesNotExist:
            return Response({"error": "Group not found"}, status=404)

class TriggerNotification(APIView):
    def post(self, request):
        message = request.data.get("message", "Default message")
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(
            "notifications",
            {
                "type": "send_notification",
                "message": message
            }
        )
        return Response({"status": "notification sent"})