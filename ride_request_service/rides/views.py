from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rides.models import Ride, RideRequest
from .serializers import RideHistorySerializer, RideRequestSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=201)
        return Response(serializer.errors, status=400)
    
@api_view(['POST'])
def generate_token(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = User.objects.get(username=username)
    if user.check_password(password):
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=401)

class RideRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RideRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        ride_requests = RideRequest.objects.filter(user=request.user)
        serializer = RideRequestSerializer(ride_requests, many=True)
        return Response(serializer.data, status=200)

class RideHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rides = Ride.objects.filter(driver=request.user)
        serializer = RideHistorySerializer(rides, many=True)
        return Response(serializer.data, status=200)

class RateRideView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        ride_id = request.data.get('ride_id')
        rating = request.data.get('rating')
        
        try:
            ride = Ride.objects.get(id=ride_id, driver=request.user)
        except Ride.DoesNotExist:
            return Response({'message': 'Ride not found'}, status=404)

        ride.rating = rating
        ride.save()
        
        return Response({'message': 'Ride rated successfully'}, status=200)
