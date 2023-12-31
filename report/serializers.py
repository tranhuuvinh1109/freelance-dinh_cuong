from rest_framework import serializers

import report
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email','avatar', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            avatar=validated_data['avatar']
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reported
        # fields = ['id','location', 'date_report', 'device', 'cable', 'power', 'report', 'other_job','exist','propose', 'creator', 'date']
        exclude = ['createAt', 'updateAt']

