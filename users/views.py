from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import User
from .tokens import create_access_token, create_refresh_token, verify_access_token, verify_refresh_token, \
    revoke_refresh_token
from mongoengine import DoesNotExist, NotUniqueError


@api_view(["POST"])
def register_user(request):
    email = request.data.get("email")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    password = request.data.get("password")

    if not all([email, first_name, last_name, password]):
        return JsonResponse({"error": "Missing required fields"}, status=400)

    if User.objects(email=email).first():
        return JsonResponse({"error": "Email already exists"}, status=400)

    try:
        user = User(
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save()
        return JsonResponse({"message": "User created successfully"}, status=201)
    except NotUniqueError:
        return JsonResponse({"error": "Email already exists"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@api_view(["POST"])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")

    if not email or not password:
        return JsonResponse({"error": "Email and password required"}, status=400)

    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return JsonResponse({"error": "Invalid credentials"}, status=401)

        access_token = create_access_token(user.id, user.subscription_type)
        refresh_token = create_refresh_token(user.id)

        return JsonResponse({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "subscription_type": user.subscription_type
        }, status=200)
    except DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


@api_view(["POST"])
def refresh_token(request):
    refresh_token = request.data.get("refresh_token")
    if not refresh_token:
        return JsonResponse({"error": "Refresh token required"}, status=400)

    payload = verify_refresh_token(refresh_token)
    user = User.objects.get(id=payload["user_id"])

    new_access_token = create_access_token(user.id, user.subscription_type)
    return JsonResponse({"access_token": new_access_token}, status=200)


@api_view(["POST"])
def logout_user(request):
    refresh_token = request.data.get("refresh_token")
    if not refresh_token:
        return JsonResponse({"error": "Refresh token required"}, status=400)

    revoke_refresh_token(refresh_token)
    return JsonResponse({"message": "Logged out"}, status=200)


@api_view(["GET"])
def protected_view(request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"error": "Missing or invalid token"}, status=401)

    token = auth_header.split(" ")[1]
    payload = verify_access_token(token)

    return JsonResponse({
        "message": "Access granted",
        "subscription_type": payload["subscription_type"]
    })
