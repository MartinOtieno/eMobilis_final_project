from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse


def register(request):
    """Show the registration form and handle user registration."""
    if request.method == 'POST':
        # Retrieve form data
        username = request.POST.get('username', '').strip()
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        password_confirmation = request.POST.get('password_confirmation', '').strip()

        # Validate form data
        if not username or not password or not email:
            messages.error(request, "Username, email, and password are required!")
            return render(request, 'accounts/register.html', {
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email
            })

        if password != password_confirmation:
            messages.error(request, "Passwords do not match!")
            return render(request, 'accounts/register.html', {
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email
            })

        try:
            # Create the user
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()

            # Success message and redirect to login
            messages.success(request, "You have successfully created your account! Please log in.")
            return redirect(reverse('login'))
        except Exception as e:
            # Handle errors during user creation
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, 'accounts/register.html', {
                'username': username,
                'first_name': first_name,
                'last_name': last_name,
                'email': email
            })

    # Render the registration form for GET requests
    return render(request, 'accounts/register.html')

#login page
def login_view(request):
    """ show the login page """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        #check
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index_page')
        else:
            messages.error(request, "Invalid login credentials")
            
    return render(request, "accounts/login.html")

