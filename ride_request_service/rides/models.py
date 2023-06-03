from django.db import models
from django.contrib.auth.models import User

class RideRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('requested', 'Requested'), ('accepted', 'Accepted'), ('completed', 'Completed')])

    class Meta:
        app_label = 'rides'

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    ride_request = models.ForeignKey(RideRequest, on_delete=models.CASCADE)
    fare = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

