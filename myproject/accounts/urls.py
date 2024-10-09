from accounts.views import FeedView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (  # PhotoRatingView,
    LoginView,
    ProfileDetailView,
    ProfileListView,
    RegisterView,
)

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"
    ),
    path("feed/", FeedView.as_view(), name="feed"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profiles/", ProfileListView.as_view(), name="profile_list"),
    path(
        "profiles/<str:username>/", ProfileDetailView.as_view(), name="profile_detail"
    ),
    # path("rate/", PhotoRatingView.as_view(), name="photo_rating"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
