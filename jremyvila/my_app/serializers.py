# my_app/serializers.py

from rest_framework import serializers
from .models import HangmanWordBank
from .models import UserProfile

class HangmanWordBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = HangmanWordBank
        fields = ('name', 'hint')  # Include fields you want to serialize

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'password', 'is_online')