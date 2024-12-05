from django.shortcuts import render, redirect, get_object_or_404
from .models import BloodDonation
from django.db.models import Q

from django.core.mail import send_mail
from .forms import DonorForm

# from .models import UploadedImage
# from models import UploadedImage
from django.core.files.storage import FileSystemStorage

from blood import models

# Create your views here.
# Home
def index_page(request):
    """ Display the home page """
    return render(request, "index.html")

# About
def about_page(request):
    """ Display the about page """
    return render(request, "about.html")
# team
def team_page(request):
          """ Display the team """
          return render(request, "team.html")
# gallery
def gallery_page(request):
          """ Display the gallery page """
          return render(request, 'gallery.html')
# contact
def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Send email
        send_mail(
            subject=f"Contact Form: {subject}",
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{message}",
            from_email=email,
            recipient_list=['martin.onyango.otieno@gmail.com'],
        )

        # Provide a success message
        return render(request, 'contact.html', {'success': 'Your message has been sent successfully!'})
    return render(request, 'contact.html')
# booking
# def donate_page(request):
#     """ Display the booking page """
#     return render(request, 'donate.html')

#Function to push the booking to the DB
def donate_page(request):
    """ Function to pust the bookings DB """
    if request.method == 'POST':
         # Handle form submission and image saving
        donations = BloodDonation(
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            age = request.POST['age'],
            address = request.POST['address'],
            # gender = request.POST['gender'],
            blood_type = request.POST['blood_type'],
            donation_date = request.POST['donation_date'],
            location = request.POST['location'],
            image = request.FILES['image'],  # Handle the uploaded image

        )
        # save the variable
        donations.save()
        # redirect
        return redirect('index_page')
    else:
        return render(request, 'donate.html')
    
# Retrieve all donation
def retrieve_donations(request):
    # Create a variable to store these donations
    donations = BloodDonation.objects.all()
    context = {'donations':donations} 
    return render(request, 'show_donations.html', context)
#delete
def delete_donations(request, id):
    """Delete a booking by ID and redirect to the donations list."""
    donation = get_object_or_404(BloodDonation, id=id)  # Use get_object_or_404 for better error handling
    donation.delete()  # Delete the donations
    return redirect("show_donations") # Redirect to the page that lists all donations
#update
def update_donation(request, donation_id):
    """Update the donation record."""
    donation = get_object_or_404(BloodDonation, id=donation_id)
    
    if request.method == 'POST':
        # Update donation fields with form data
        donation.name = request.POST.get('name')
        donation.email = request.POST.get('email')
        donation.phone = request.POST.get('phone')
        donation.blood_type = request.POST.get('blood_type')
        donation.donation_date = request.POST.get('donation_date')
        donation.location = request.POST.get('location')
        
        donation.save()# Save the updated donation record
        
        return redirect("show_donations")# Redirect to the donations list page
    
    # Pass the donation object to the template
    context = {'donation': donation}
    return render(request, "update_donation.html", context)

#upload image
def upload_image(request):
    if request.method == 'POST':
        # Retrieve data from the form
        title = request.POST['title']
        uploaded_file = request.FILES['image']
        
        # Save the file using filesystemStorage
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        
        # Save file information to the database
        image = UploadedImage.objects.create(title=title, image=filename)
        image.save()
        
        return render(request, 'donate.html', {'file_url':file_url})
    return render(request, "donate.html")
# search bar
def search_blood_donations(request):
    blood_type_query = request.GET.get('blood_type')  # Get selected blood type
    location_query = request.GET.get('location')      # Get selected location
    results = []

    # Filter by blood_type and location if provided
    if blood_type_query or location_query:
        results = BloodDonation.objects.filter(
            (Q(blood_type__icontains=blood_type_query) if blood_type_query else Q()) &
            (Q(location__icontains=location_query) if location_query else Q())
        )

    return render(request, 'blood_donation_search.html', {
        'results': results,
        'blood_type_query': blood_type_query,
        'location_query': location_query,
        'blood_group_choices': BloodDonation.BLOOD_GROUP_CHOICES,
        'kenyan_counties': BloodDonation.KENYAN_COUNTIES,
    })
    
def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_donations')  # Redirect to the records page
        else:
            print(form.errors)  # Debugging: Prints errors in the terminal
    else:
        form = DonorForm()

    return render(request, 'add_donor.html', {'form': form})


#search button
def search_blood_donations(request):
    blood_type_query = request.GET.get('blood_type', '')  # Get blood_type from query string
    donations = BloodDonation.objects.all()

    if blood_type_query:  # Apply filter only if blood_type is provided
        donations = donations.filter(blood_type=blood_type_query)

    return render(request, 'show_donations.html', {
        'donations': donations,
        'blood_type_query': blood_type_query,
        'blood_group_choices': [
            ('A+', 'A+'), ('A-', 'A-'), 
            ('B+', 'B+'), ('B-', 'B-'), 
            ('AB+', 'AB+'), ('AB-', 'AB-'), 
            ('O+', 'O+'), ('O-', 'O-')
        ],  # Replace this with your dynamic choices if applicable
    })