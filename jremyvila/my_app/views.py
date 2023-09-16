#/my_app/views.py
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
import json

from .models import HangmanWordBank, UserProfile, Leaderboard
from .serializers import HangmanWordBankSerializer, UserProfileSerializer
from .serializers import LeaderboardSerializer
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

class LeaderboardView(generics.ListAPIView):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer


# Hangman operations
@csrf_exempt
def update_leaderboard(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = data.get('user')
            game_result = data.get('game_result')


            # import uuid

            # Generate a random UUID (version 4)
            # guid = uuid.uuid4()

            # Convert the UUID to a string representation
            # guid_str = str(guid)

            # if(!user):
            #     user = "tester"



            


            # Check if the user already exists in the Leaderboard
            try:
                leaderboard_entry = Leaderboard.objects.get(user=user)
            except Leaderboard.DoesNotExist:
                # If the user does not exist, create a new entry
                leaderboard_entry = Leaderboard(user=user, wins=0, losses=0)

            if game_result == 1:
                leaderboard_entry.wins += 1
            elif game_result == 0:
                leaderboard_entry.losses += 1

            leaderboard_entry.save()

            response_data = {'message': 'Leaderboard updated successfully'}
            return JsonResponse(response_data, status=200)

        except json.JSONDecodeError:
            response_data = {'error': 'Invalid JSON data'}
            return JsonResponse(response_data, status=400)

    else:
        response_data = {'message': 'GET requests not supported'}
        return JsonResponse(response_data, status=405)


def view_leaderboard(request):
    # Query the leaderboard table to get all records
    leaderboard_data = Leaderboard.objects.all()

    # Convert the queryset to a list of dictionaries
    leaderboard_list = [{'user': entry.user, 'wins': entry.wins, 'losses': entry.losses} for entry in leaderboard_data]

    # Create a JSON response with the leaderboard data
    response_data = {'leaderboard': leaderboard_list}
    return JsonResponse(response_data)


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


def delete_user(request):
    if request.method == 'DELETE':
        try:
            data = json.loads(request.body)
            username = data.get('user')


            if username is not None:
                try:
                    user_profile = UserProfile.objects.get(user=username)
                    user_profile.delete()
                    return JsonResponse({'message': f'User {username} deleted successfully'})
                except UserProfile.DoesNotExist:
                    return JsonResponse({'message': f'User {username} not found'}, status=404)
            else:
                return JsonResponse({'message': 'user is required in the request data'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)



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