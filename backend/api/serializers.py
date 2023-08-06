from rest_framework import serializers
from api.models import PostJobModel, UserModel

class PostJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostJobModel
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        