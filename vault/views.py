from .models import VaultItem
from .encryption import encrypt_data, decrypt_data
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

def home(request):
    return render(request, 'vault/home.html')

def register(request):
  if request.method == 'POST':
    title = request.POST['title']
    secret = request.POST['secret']
    uploaded_file = request.FILES.get('file')

    encrypted = encrypt_data(secret)

    VaultItem.objects.create(
        user=request.user,
        title=title,
        encrypted_data=encrypted,
        uploaded_file=uploaded_file
    )
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'vault/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
