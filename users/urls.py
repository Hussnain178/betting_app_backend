# urls.py

from django.urls import path
from users import views

urlpatterns = [
    path("register", views.register_user, name="register_user"),
    path("login", views.login_user, name="login_user"),
    path("refresh", views.refresh_token, name="refresh_token"),
    path("logout", views.logout_user, name="logout_user"),
    path("protected", views.protected_view, name="protected_view"),
    path("server_check", views.server_check_view, name="server_check_view"),
]
# docker run -d -p 6379:6379 redis