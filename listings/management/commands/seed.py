import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing

class Command(BaseCommand):
    help = "Seeds the database with sample data for the Listing model."

    def handle(self, *args, **kwargs):
        # Ensure there are users to assign as hosts
        if User.objects.count() == 0:
            self.stdout.write(self.style.ERROR("No users found. Create at least one user first."))
            return

        # Define sample data
        locations = ["New York", "Los Angeles", "Paris", "Tokyo", "Cape Town"]
        descriptions = [
            "A cozy place in the city center.",
            "A luxurious villa with a sea view.",
            "A charming countryside cottage.",
            "A modern apartment near major attractions.",
            "A beautiful retreat surrounded by nature.",
        ]

        # Create listings
        num_listings = 10
        for _ in range(num_listings):
            host = random.choice(User.objects.all())
            location = random.choice(locations)
            description = random.choice(descriptions)

            listing = Listing.objects.create(
                host=host,
                name=f"Sample Listing {_ + 1}",
                description=description,
                location=location,
                price_per_night=round(random.uniform(50, 500), 2),
            )
            self.stdout.write(self.style.SUCCESS(f"Created Listing: {listing.name}"))

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
