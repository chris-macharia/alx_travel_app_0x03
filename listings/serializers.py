from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    """Serializer for the Listing model."""

    class Meta:
        model = Listing
        fields = [
            'id',
            'host',
            'name',
            'description',
            'location',
            'price_per_night',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for the Booking model."""

    class Meta:
        model = Booking
        fields = [
            'id',
            'listing',
            'user',
            'start_date',
            'end_date',
            'total_price',
            'status',
            'created_at',
        ]
        read_only_fields = ['id', 'user', 'total_price', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user and request.user.is_authenticated:
            validated_data['user'] = request.user
        else:
            raise serializers.ValidationError("User must be authenticated to create a booking.")

        # Calculate total price
        start_date = validated_data.get('start_date')
        end_date = validated_data.get('end_date')
        listing = validated_data.get('listing')

        if not start_date or not end_date:
            raise serializers.ValidationError("Start date and end date are required.")

        if end_date <= start_date:
            raise serializers.ValidationError("End date must be after start date.")

        num_nights = (end_date - start_date).days
        validated_data['total_price'] = num_nights * listing.price_per_night

        return super().create(validated_data)
