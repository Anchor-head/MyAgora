from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DebateUser,SpeechHistory

class DebateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebateUser
        fields = '__all__'

    def create(self, validated_data):
        user = DebateUser.objects.create(
            username = validated_data['username'],
            password = validated_data['password']
        )
        user.save()
        return user


class SpeechHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeechHistory
        fields = '__all__'