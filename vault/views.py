from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import VaultItem
from .encryption import encrypt_data

# HOME PAGE
def home(request):
    return render(request, 'vault/home.html')

# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'vault/login.html')

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    if request.method == "POST":
        print("FILES:", request.FILES)   # 👈 ADD THIS

        title = request.POST.get('title')
        secret_data = request.POST.get('secret_data')
        file = request.FILES.get('file')

        encrypted = encrypt_data(secret_data)

        VaultItem.objects.create(
            user=request.user,
            title=title,
            encrypted_data=encrypted,
            uploaded_file=file
        )

        return redirect('dashboard')

    items = VaultItem.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'items': items})
