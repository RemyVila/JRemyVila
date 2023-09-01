# my_app/serializers.py

from rest_framework import serializers
from .models import HangmanWordBank

class HangmanWordBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = HangmanWordBank
        fields = ('name', 'hint')  # Include fields you want to serialize