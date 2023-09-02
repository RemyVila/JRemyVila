# my_app/urls.py

from django.urls import path
from .views import HangmanWordBankList, UserProfiles
from . import views


urlpatterns = [
    path('hangman-wordbank/', HangmanWordBankList.as_view(), name='hangman-wordbank'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('all_users/', views.all_users, name='all_users'),
    path('logout/', views.log_out, name='log_out'),
    # path('admin/delete-user/', views.admin_delete_user, name='admin_delete_user'),
    path('', views.youre_here, name='youre_here'),
]