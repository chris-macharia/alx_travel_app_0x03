
from django.shortcuts import render
# Create your views here.
from rest_framework import generics, viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated
from .tasks import send_booking_email

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def perform_create(self, serializer):
        serializer.save(host=self.request.user)  # Assign logged-in user as host


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on Listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for performing CRUD operations on Bookings.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can book

    def perform_create(self, serializer):
        booking = serializer.save()
        send_booking_email.delay(
            booking.user.email,
            booking.listing.name,
            booking.start_date,
            booking.end_date
        )
