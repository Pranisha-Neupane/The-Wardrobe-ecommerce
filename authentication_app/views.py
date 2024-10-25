from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# User registration view
def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'authentication/register.html')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            # Create and save the new user with hashed password
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)  # Hash the password
            user.is_active = True  # Set to True if you want users to log in immediately
            user.save()

            messages.success(request, "User registered successfully. Please login.")
            return redirect('user_login')  # Redirect to login page after successful registration

    return render(request, 'authentication/register.html')

# User login view

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Attempting login with Username: {username}, Password: {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None or user.is_active:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    return render(request, 'authentication/login.html')


# User logout view
def user_logout(request):
    logout(request)
    return redirect('/')  # Redirect to homepage after logout

