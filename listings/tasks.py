from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_test_email():
    return "Test email sent successfully!"

@shared_task
def send_booking_email(user_email, property_name, check_in, check_out):
    subject = "Booking Confirmation"
    message = f"Your booking for {property_name} from {check_in} to {check_out} is confirmed."
    send_mail(subject, message, 'noreply@example.com', [user_email])
    return f"Email sent to {user_email}"
