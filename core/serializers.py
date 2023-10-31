from rest_framework import serializers
from django.contrib.auth.models import User
from core import models as core

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



class BreastfeedRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = core.BreastfeedRegistration
        fields = '__all__'
