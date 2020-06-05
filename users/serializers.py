from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, BaseUserManager
from django.contrib.auth import password_validation

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User
    """
    class Meta:
        model = User
        fields = ['id','username']


class UserRegisterSerializer(serializers.ModelSerializer):
	"""
	Serializer for registering users
	"""
	class Meta:
		model	=	User
		fields	=	['username','password','email']

	def validate_email(self,value):
		"""
		Method for validating email id
		"""
		userAccount = User.objects.filter(email=value)
		if userAccount:
			raise serializers.ValidationError("Email is already taken")
		return BaseUserManager.normalize_email(value)

	def validate_password(self,value):
		"""
		Method for validating password
		"""
		password_validation.validate_password(value)
		return value


class UserLoginSerializer(serializers.Serializer):
	"""
	Serializer for logging in users
	"""
	username = serializers.CharField(required=True)
	password = serializers.CharField(required=True)


class AuthTokenSerializer(serializers.ModelSerializer):
	"""
	Authentication token serializer
	"""
	auth_token = serializers.CharField(source='key')
	class Meta:
		model = Token
		fields = ("auth_token","created")