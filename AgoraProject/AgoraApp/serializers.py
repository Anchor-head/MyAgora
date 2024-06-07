from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DebateUser

class DebateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateUser
        fields = '__all__'

    def create(self, validated_data):
        user = DebateUser.objects.create(
            username=validated_data['username'],
            password = validated_data['password']
        )
        user.save()
        return user
