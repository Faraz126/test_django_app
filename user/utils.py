from django.contrib.auth import authenticate, get_user_model, login
from rest_framework import serializers


def get_and_authenticate_user(request, email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    else:
        login(request, user) # Redirect to a success page.
    return user

def create_user_account(email, password, first_name="",
                        last_name="", **extra_fields):

    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)

    user.save()
    return user