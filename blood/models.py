from django.db import models
from django.utils.timezone import now


class BloodDonation(models.Model):
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    ]

    KENYAN_COUNTIES = [
        ('Nairobi', 'Nairobi'),
        ('Mombasa', 'Mombasa'),
        ('Kisumu', 'Kisumu'),
        ('Nakuru', 'Nakuru'),
        ('Kericho', 'Kericho'),
        ('Kiambu', 'Kiambu'),
        ('Machakos', 'Machakos'),
        ('Nyeri', 'Nyeri'),
        ('Meru', 'Meru'),
        ('Homabay', 'Homabay'),
        ('Baringo', 'Baringo'),
        ('Taita Taveta', 'Taita Taveta'),
        ('Kakamega', 'Kakamega'),
        ('Vihiga', 'Vihiga'),
        ('Siaya', 'Siaya'),
        ('Kwale', 'Kwale'),
        ('Samburu', 'Samburu'),
        ('Turkana', 'Turkana'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    blood_type = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    donation_date = models.DateField()
    location = models.CharField(max_length=50, choices=KENYAN_COUNTIES)
    image = models.ImageField(upload_to='uploads/donation_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    age = models.IntegerField(default='20')
    address = models.TextField(default='No address provided')
    
    status = models.CharField(
        max_length=20,
        choices=[('Available', 'Available'), ('Booked', 'Booked')],
        default='Available'
    )

    def __str__(self):
        return f"{self.name} - {self.blood_type} ({self.location})"
