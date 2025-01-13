from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingListCreateView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
