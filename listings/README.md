# Listings Directory

This directory contains the core functionality for managing property listings, bookings, and reviews in the travel application.

## Models

The models defined in this directory represent the main components of the application:

### **Listing**
Represents a property listing hosted by a user.

- **Fields:**
  - `host`: The user who owns or is hosting the property (ForeignKey to `User`).
  - `name`: Name of the listing.
  - `description`: A detailed description of the property.
  - `location`: The location of the property.
  - `price_per_night`: The cost to rent the property per night.
  - `created_at`: Timestamp of when the listing was created.
  - `updated_at`: Timestamp of when the listing was last updated.

### **Booking**
Represents a booking made by a user for a particular listing.

- **Fields:**
  - `listing`: The listing being booked (ForeignKey to `Listing`).
  - `user`: The user who made the booking (ForeignKey to `User`).
  - `start_date`: The start date of the booking.
  - `end_date`: The end date of the booking.
  - `total_price`: The total cost for the booking.
  - `status`: The current status of the booking (`pending`, `confirmed`, `canceled`).
  - `created_at`: Timestamp of when the booking was made.

### **Review**
Represents a review left by a user for a particular listing.

- **Fields:**
  - `listing`: The listing being reviewed (ForeignKey to `Listing`).
  - `user`: The user who left the review (ForeignKey to `User`).
  - `rating`: A rating value between 1 and 5.
  - `comment`: The content of the review.
  - `created_at`: Timestamp of when the review was created.

## Serializers

The `serializers.py` file contains serializers for transforming model instances into JSON representations for API communication.

### **ListingSerializer**
Serializes the `Listing` model, including fields like `host`, `name`, `description`, etc.

### **BookingSerializer**
Serializes the `Booking` model, including fields like `listing`, `user`, `status`, etc.

## Management Commands

### **Seed Command**

The `seed.py` management command populates the database with sample data for the `Listing` model. It randomly generates data for 10 listings.

- **Command:**
  ```bash
  python manage.py seed
  ```

- **Sample Listings Created**: The command will create 10 listings with random names, descriptions, and prices.

---

### **Installation**

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the seeder to populate the database with sample data:
   ```bash
   python manage.py seed
   ```

---

### **Contributing**

Feel free to contribute by creating a pull request. Ensure your code follows the project's style guidelines and includes appropriate tests.
