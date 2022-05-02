from datetime import datetime
from django.contrib.auth import authenticate, login
from rest_framework.serializers import Serializer, ValidationError, CharField
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND


class LoginSerializer(Serializer):
    """
        This serializer defines two fields for authentication:
        * username
        * password.
        It will try to authenticate the user with when validated.
    """
    username = CharField(
        label="username",
        write_only=True
    )
    password = CharField(
        label="password",
        # This will be used when the DRF browsable API is enabled
        style={
            'input_type': 'password'
        },
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        # Take username and password from request
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            # Try to authenticate the user using Django auth framework.
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                # If we don't have a regular user, raise a ValidationError
                msg = 'Access denied: wrong username or password.'
                raise ValidationError(msg, code='authorization')
        else:
            msg = 'Both "username" and "password" are required.'
            raise ValidationError(msg, code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        return Response(data={'message': 'ready for login'}, status=HTTP_202_ACCEPTED)

    def post(self, request, format=None):
        print('\n\n------', request, '------\n\n')
        serializer = LoginSerializer(
            data=self.request.data,
            context={'request': self.request}
        )
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            user = user.__dict__
            if user['is_superuser']:
                role = 'admin'
            else:
                role = 'user'
            profile = {
                'username': user['username'],
                'dates': {
                    'joined': user['date_joined'].strftime("%m/%d/%Y"),
                    'last_login': user['last_login'].strftime("%m/%d/%Y, %H:%M:%S"),
                },
                'name': {
                    'first': user['first_name'],
                    'last': user['last_name']
                },
                'contact': {
                    'email': user['email']
                },
                'role': role
            }
            return Response(
                data={
                    'status': 202,
                    'message': 'welcome',
                    'user': profile
                },
                status=HTTP_202_ACCEPTED
            )
        else:
            return Response(
                data={
                    'status': 404,
                    'message': 'invalid login',
                    'user': {}
                },
                status=HTTP_404_NOT_FOUND
            )
