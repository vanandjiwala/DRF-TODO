from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer,UserLoginSerializer,UserRegisterSerializer,AuthTokenSerializer
from django.contrib.auth.models import User
from django.core.exceptions import ImproperlyConfigured
from .utils import create_user_account,authenticateUser
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):

    serializer_class =  UserSerializer
    queryset = User.objects.all().order_by('id')

    serializer_classes = {
        'signup': UserRegisterSerializer,
        'login': UserLoginSerializer
    }


    def get_serializer_class(self):
        """
        Dynamically selecting serialized class based on the serializer_classes dictionary
        Ref: https://medium.com/aubergine-solutions/decide-serializer-class-dynamically-based-on-viewset-actions-in-django-rest-framework-drf-fb6bb1246af2
        ref: https://github.com/Ajinkya009/ProjectManagement
        :return:
        """
        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]
        return super().get_serializer_class()

    @action(methods=['POST', ], detail=False)
    def signup(self, request):
        """
        Custom method for registering new users
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        user = create_user_account(**serializer.validated_data)
        data,created = Token.objects.get_or_create(user=user)
        print(data)
        print(created)
        serializedToken = AuthTokenSerializer(data).data
        return Response(data=serializedToken, status=status.HTTP_201_CREATED)

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        """
        Custom method for logging user in
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticateUser(**serializer.validated_data)
        data, _ = Token.objects.get_or_create(user=user)
        serializedToken = AuthTokenSerializer(data).data
        return Response(data=serializedToken, status=status.HTTP_200_OK)

    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        permission_classes = (IsAuthenticated,)
        logout(request)
        return Response(data="Success", status=status.HTTP_200_OK)