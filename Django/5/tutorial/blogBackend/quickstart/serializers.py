from rest_framework import serializers
from .models import User, Profile, Post, Group
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'address']
        read_only_fields = ['id']

    def validate_name(self, value):
        user_id = self.instance.id if self.instance else None
        if User.objects.exclude(id = user_id).filter(name=value).exists():
            raise serializers.ValidationError("A user with this name already exists.")
        return value
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone_number', 'birth_place']
        read_only_fields = ['id']

    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Group
        fields = '__all__'



class UserWithProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)
    post = PostSerializer(read_only=True, many=True, source = 'posts')
    group = GroupSerializer(read_only = True, many = True, source = 'groups')
    class Meta: 
        model = User
        fields = ['id', 'name', 'address', 'profile', 'post', 'group']