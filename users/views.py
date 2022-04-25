# Users Views

# Imports DJANGO
import imp
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
# Models
from django.contrib.auth.models import User
from users.models import Profile
# Exeptions
from django.db.utils import IntegrityError

def login_view(request):
    # Login view
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password=password)
        if user:
            login(request, user)
            return redirect('feed') 
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and password'})
            
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
           return render(request, 'users/signup.html',{'error':'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html',{'error':'Username is already exists'})
         
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        profile= Profile(user=user)
        profile.save()
        return render(request, 'users/login.html')
        
    return render(request, 'users/signup.html')