from django.urls import path
from .views import RateRideView, RideHistoryView, RideRequestView, UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
     path('token/', obtain_auth_token, name='api-token'),
    path('ride-requests/', RideRequestView.as_view(), name='ride-requests'),
    path('ride-history/', RideHistoryView.as_view(), name='ride-history'),
    path('rate-ride/', RateRideView.as_view(), name='rate-ride'),
]
