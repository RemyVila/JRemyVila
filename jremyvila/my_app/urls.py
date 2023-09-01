# my_app/urls.py

from django.urls import path
from .views import HangmanWordBankList

urlpatterns = [
    path('hangman-wordbank/', HangmanWordBankList.as_view(), name='hangman-wordbank'),
]