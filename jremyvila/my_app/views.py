#/my_app/views.py
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse

from .models import HangmanWordBank, UserProfile
from .serializers import HangmanWordBankSerializer, UserProfileSerializer

import json


# HANGMAN
class HangmanWordBankList(generics.ListAPIView):
    queryset = HangmanWordBank.objects.all()
    serializer_class = HangmanWordBankSerializer


# Login and Register
class UserProfiles(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

from django.http import JsonResponse

from django.http import JsonResponse
from .models import UserProfile  # Import your custom model

def register(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            username = data['user']
            password = data['password']

            # Create a new UserProfile instance and save it to the database
            user_profile = UserProfile(user=username, password=password, is_online=True)
            user_profile.save()

            # Send a JSON response
            response_data = {'message': 'User created successfully'}
            return JsonResponse(response_data, status=201)  # 201 Created status code
        except json.JSONDecodeError:
            # Handle JSON decoding error
            response_data = {'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)  # 400 Bad Request status code
    else:
        # Handle GET requests or other HTTP methods if needed
        response_data = {'message': 'GET requests not supported'}
        return JsonResponse(response_data, status=405)  # 405 Method Not Allowed status code


from django.http import JsonResponse

# Fake Auth
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['user']
            password = data['password']

            is_online = True  # Change user_authenticated to is_online

            if is_online:
                # Update the 'is_online' field to True
                user_profile = UserProfile.objects.get(user=username)
                user_profile.is_online = True
                user_profile.save()

                response_data = {'message': 'User logged in successfully'}
                return JsonResponse(response_data, status=200)
            else:
                response_data = {'error': 'Authentication failed'}
                return JsonResponse(response_data, status=401)  # 401 Unauthorized status code
        except json.JSONDecodeError:
            response_data = {'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)  # 400 Bad Request status code
    else:
        response_data = {'message': 'GET requests not supported'}
        return JsonResponse(response_data, status=405)  # 405 Method Not Allowed status code



def all_users(request):
    if request.method == 'GET':
        # Query all user profiles
        user_profiles = UserProfile.objects.all()

        # Convert user profiles to a list of dictionaries
        users_list = [{'user': profile.user, 'password': profile.password ,'is_online': profile.is_online} for profile in user_profiles]

        # Return the list of users as a JSON response
        return JsonResponse(users_list, safe=False)
    else:
        response_data = {'message': 'Only GET requests are supported'}
        return JsonResponse(response_data, status=405)  # 405 Method Not Allowed status code