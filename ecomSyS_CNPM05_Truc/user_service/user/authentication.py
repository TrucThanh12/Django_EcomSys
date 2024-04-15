# xác thưc tùy chỉnh
from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
import jwt
from django.conf import settings
from rest_framework import exceptions
from .models import User

class SafeJWTAuthentication(BaseAuthentication):
    User = get_user_model()
    def authenticate(self, request):
        authorization_header = request.headers.get('Authorization')

        if not authorization_header:
            return None

        try:
            token_prefix, access_token = authorization_header.split(' ')
            if token_prefix != 'Bearer':
                raise exceptions.AuthenticationFailed('Invalid token prefix')

            payload = jwt.decode(access_token,
                                 settings.SECRET_KEY,
                                 algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('Access token expired')
        except ValueError:
            raise exceptions.AuthenticationFailed('Invalid token format')
        except jwt.InvalidTokenError:
            raise exceptions.AuthenticationFailed('Invalid token')

        user_name = payload.get('user_name')
        if user_name is None:
            raise exceptions.AuthenticationFailed('Username not found in token payload')

        user = User.objects.filter(username=user_name).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User is not active')

        return (user, None)