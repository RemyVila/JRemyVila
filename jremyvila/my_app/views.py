#/my_app/views.py

from django.shortcuts import render
from rest_framework import generics
from .models import HangmanWordBank
from .serializers import HangmanWordBankSerializer

# Create your views here.
class HangmanWordBankList(generics.ListAPIView):
    queryset = HangmanWordBank.objects.all()
    serializer_class = HangmanWordBankSerializer
