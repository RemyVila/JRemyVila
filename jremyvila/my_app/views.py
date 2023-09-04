#/my_app/views.py
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
import json

from .models import HangmanWordBank, UserProfile
from .serializers import HangmanWordBankSerializer, UserProfileSerializer

# Disable CSRF validation
from django.views.decorators.csrf import csrf_exempt


# HANGMAN
class HangmanWordBankList(generics.ListAPIView):
    queryset = HangmanWordBank.objects.all()
    serializer_class = HangmanWordBankSerializer




# Login and Register
class UserProfiles(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def register(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            username = data.get('user')
            password = data.get('password')

            # Check if a user with the provided username already exists
            if UserProfile.objects.filter(user=username).exists():
                response_data = {'error': 'User already exists under that name'}
                return JsonResponse(response_data, status=400)  # 400 Bad Request status code

            # Create a new UserProfile instance and save it to the database
            user_profile = UserProfile(user=username, password=password, is_online=False)
            user_profile.save()

            response_data = {'message': 'User created successfully'}
            return JsonResponse(response_data, status=201)  # 201 Created status code
        except IntegrityError:
            # Handle IntegrityError, which occurs if there's a database integrity violation (e.g., duplicate user)
            response_data = {'error': 'User already exists under that name'}
            return JsonResponse(response_data, status=400)  # 400 Bad Request status code
        except json.JSONDecodeError:
            response_data = {'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)  # 400 Bad Request status code
    else:
        response_data = {'message': 'GET requests not supported'}
        return JsonResponse(response_data, status=405)  # 405 Method Not Allowed status code


# Fake Auth
def user_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['user']
            password = data['password']

            # Retrieve the user profile based on the username
            try:
                user_profile = UserProfile.objects.get(user=username)
            except UserProfile.DoesNotExist:
                user_profile = None

            if user_profile and user_profile.password == password:
                # Password matches, consider it a successful login
                user_profile.is_online = True  # Set is_online to True
                user_profile.save()  # Save the updated user profile

                response_data = {'message': 'User logged in successfully'}
                return JsonResponse(response_data, status=200)
            else:
                # Password does not match or user does not exist
                response_data = {'error': 'Wrong username or password'}
                return JsonResponse(response_data, status=401)  # 401 Unauthorized status code

        except json.JSONDecodeError:
            response_data = {'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)  # 400 Bad Request status code
    else:
        response_data = {'message': 'GET requests not supported'}
        return JsonResponse(response_data, status=405)

# log out user
def log_out(request):
    # Check for HTTP request type
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            username = data.get('user')

            # Retrieve the UserProfile instance based on the username
            user_profile = UserProfile.objects.get(user=username)

            # Set 'is_online' to False
            user_profile.is_online = False
            user_profile.save()

            response_data = {'message': 'User logged out successfully'}
            return JsonResponse(response_data, status=200)
        
        # if there are data integrity conflicts, will throw errors
        except IntegrityError:
            response_data = {'error': 'User already exists under that name'}
            return JsonResponse(response_data, status=400)  # 400 Bad Request status code
        except UserProfile.DoesNotExist:
            response_data = {'error': 'User not found'}
            return JsonResponse(response_data, status=404)  # 404 Not Found status code
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



def youre_here(request):
    if request.method == 'GET':
        return HttpResponse('You are here!')