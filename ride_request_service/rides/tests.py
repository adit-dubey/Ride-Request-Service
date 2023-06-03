from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from rides.models import Ride

class RideRequestTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_ride_request_creation(self):
        url = reverse('ride-requests')
        data = {'pickup_location': 'Location A', 'destination': 'Location B'}
        self.client.force_authenticate(user=self.user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['pickup_location'], 'Location A')
        self.assertEqual(response.data['destination'], 'Location B')
        self.assertEqual(response.data['user'], self.user.id)

    def test_ride_request_list(self):
        url = reverse('ride-requests')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # No ride requests initially

class RideHistoryTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.driver = User.objects.create_user(username='testdriver', password='testpassword')
        self.ride = Ride.objects.create(driver=self.driver, user=self.user, pickup_location='Location A', destination='Location B')

    def test_ride_history(self):
        url = reverse('ride-history')
        self.client.force_authenticate(user=self.driver)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['ride']['pickup_location'], 'Location A')
        self.assertEqual(response.data[0]['ride']['destination'], 'Location B')

class RateRideTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.driver = User.objects.create_user(username='testdriver', password='testpassword')
        self.ride = Ride.objects.create(driver=self.driver, user=self.user, pickup_location='Location A', destination='Location B')

    def test_rate_ride(self):
        url = reverse('rate-ride')
        self.client.force_authenticate(user=self.driver)
        data = {'ride_id': self.ride.id, 'rating': 4}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Ride rated successfully')
        self.ride.refresh_from_db()
        self.assertEqual(self.ride.rating, 4)
