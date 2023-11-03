from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_jwt.views import RefreshJSONWebToken

from core import serializers
from core import models as core

class UserLoginView(APIView):
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user using the authenticate function
            user = authenticate(request=self.request, username=username, password=password)

            if user is not None:
                # If authentication is successful, generate a JWT token
                refresh = RefreshToken.for_user(user)
                token = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
                return Response(token, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RefreshTokenView(RefreshJSONWebToken):
    # Customize the response, if needed
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            # Customize the response data as needed
            # For example, add custom data to the response
            response.data['custom_key'] = 'custom_value'
        return response

class BreastfeedRegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BreastfeedRegistrationSerializer
    # authentication_classes = [JWTAuthentication]
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    # Only get the queryset of the authenticated user
    def get_queryset(self):
        # user = self.request.user
        # queryset = core.BreastfeedRegistration.objects.filter(baby__user=user)
        try:
            if self.request.query_params['type'] == 'list':
                queryset = core.BreastfeedRegistration.objects.all()
        except:
            queryset = core.BreastfeedRegistration.objects.filter(end_time__isnull=True)

        return queryset