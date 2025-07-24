import jwt
import redis
import os
from datetime import datetime, timedelta
from rest_framework.exceptions import AuthenticationFailed

# Load env vars
JWT_SECRET = os.getenv("JWT_SECRET", "fallback_jwt_secret")
REFRESH_SECRET = os.getenv("REFRESH_SECRET", "fallback_refresh_secret")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

# Redis client for refresh token storage
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)


def create_access_token(user_id, subscription_type):
    payload = {
        "user_id": str(user_id),
        "subscription_type": subscription_type,
        "exp": datetime.utcnow() + timedelta(seconds=5)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm="HS256")


def create_refresh_token(user_id):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(days=7)
    }
    token = jwt.encode(payload, REFRESH_SECRET, algorithm="HS256")
    redis_client.setex(token, timedelta(days=7), str(user_id))
    return token


def verify_access_token(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Access token expired")
    except jwt.InvalidTokenError:
        raise AuthenticationFailed("Invalid access token")


def verify_refresh_token(token):
    try:
        payload = jwt.decode(token, REFRESH_SECRET, algorithms=["HS256"])
        if not redis_client.exists(token):
            raise AuthenticationFailed("Refresh token revoked")
        return payload
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Refresh token expired")
    except jwt.InvalidTokenError:
        raise AuthenticationFailed("Invalid refresh token")


def revoke_refresh_token(token):
    redis_client.delete(token)
