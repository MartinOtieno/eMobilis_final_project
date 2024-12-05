from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse


def register(request):
    """Show the registration form and handle user registration."""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password_confirmation = request.POST.get('password_confirmation', '')

        # Validate form data
        if not username or not password or not email:
            messages.error(request, "Username, email, and password are required!")
            return render(request, 'accounts/register.html')

        if password != password_confirmation:
            messages.error(request, "Passwords do not match!")
            return render(request, 'accounts/register.html')

        try:
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, "You have successfully created your account!")
            print(reverse('login'))
            return redirect('accounts:login')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")

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

