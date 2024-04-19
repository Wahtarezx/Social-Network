from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenBlacklistView

from myauth.api.v1.views import (RegisterView, ProfileListView, ProfileDetailView, SubscribeUserAPIView)

app_name = 'myauth'

urlpatterns = [
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('auth/token/register/', RegisterView.as_view(), name='register_user'),
    path('profile_list/', ProfileListView.as_view(), name='profile_list'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/<int:pk>/subscribe/', SubscribeUserAPIView.as_view(), name='subscribe'),
]
