from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from apps.users.models import User, Questionnaire, Service
from apps.users.serializers import RegisterSerializer, LoginSerializer, QuestionnaireSerializer, ServiceSerializer


# Create your views here.


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(CreateAPIView):
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                access = AccessToken.for_user(user)
                response = {
                    "access_token": str(access),
                    "refresh_token": str(refresh)
                }
                return Response(response, status=status.HTTP_200_OK)
        return Response({'message': 'логин или пароль неверный'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def questionnaire_view(request):
    profile, create = Questionnaire.objects.get_or_create(user_id=request.user.id)
    if request.method == 'GET':
        serializer = QuestionnaireSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionnaireSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


@api_view(['POST'])
def service_view(request):
    serializer = ServiceSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
