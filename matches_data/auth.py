# matches_data/auth.py
from functools import wraps
from rest_framework.response import Response
from users.tokens import verify_access_token


def jwt_required(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return Response({"error": "Missing or invalid token"}, status=401)

        token = auth_header.split(" ")[1]
        try:
            payload = verify_access_token(token)
            request.user = payload  # Attach payload to request
        except Exception as e:
            return Response({"error": "Invalid or expired token"}, status=401)

        return view_func(request, *args, **kwargs)

    return wrapped_view
