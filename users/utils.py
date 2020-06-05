from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.models import User

#, **extra_fields
def create_user_account(username, email, password):
    user = User.objects.create_user(
        email=email, password=password, username=username)
    return user

def authenticateUser(username,password):
	user = authenticate(username=username, password=password)
	if user is None:
		raise serializers.ValidationError("Invalid email/password")
	return user