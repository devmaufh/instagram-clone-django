"""User views"""
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.db import IntegrityError

from users.models import Profile


# Create your views here.
def login_view(request):
    """Login view """
    if request.user.is_authenticated:
        return redirect('feed')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'User or password incorrect!'})
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('feed')
    if request.method == 'POST':
        user_name = request.POST.get('username', True)
        password = request.POST.get('passwd', True)
        password_confirmation = request.POST.get('passwd_confirmation', True)
        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation doest not match'})
        try:
            user = User.objects.create_user(username=user_name, password=password)
        except IntegrityError as ie:
            return render(request, 'users/signup.html', {'error': 'Username is already use'})

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email', True)
        user.save()
        profile = Profile(user=user)
        profile.save()
        return redirect('login')

    return render(request, 'users/signup.html')
