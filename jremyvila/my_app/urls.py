# my_app/urls.py

from django.urls import path
from .views import HangmanWordBankList, UserProfiles
## MUST IMPORT USERPROFILE LIST
# from .views import 
from . import views


urlpatterns = [
    path('hangman-wordbank/', HangmanWordBankList.as_view(), name='hangman-wordbank'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('all_users/', views.all_users, name='all_users')
]