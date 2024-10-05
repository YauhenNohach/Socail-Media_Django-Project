from accounts.views import FeedView
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import LoginView, RegisterView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path("feed/", FeedView.as_view(), name="feed"),
    path("register/", RegisterView.as_view(), name="register"),
]
