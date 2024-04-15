# xác định cách mã hóa
import datetime
import jwt
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

# tạo access token dựa trên thông tin người dùng và tời gian hết hạn
def generate_access_token(user):
    access_token_payload = {
        'user_name': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256')
    return access_token


# tạo refresh token dựa trên thông tin người dùng và tời gian hết hạn
def generate_refresh_token(user):
    refresh_token_payload = {
        'user_name': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow(),
    }
    refresh_token = jwt.encode(refresh_token_payload,
                               settings.REFRESH_TOKEN_SECRET, algorithm='HS256')
    return refresh_token
