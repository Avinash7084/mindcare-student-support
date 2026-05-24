
# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .utils import calculate_mental_health_metrics, get_chat_response
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
import json
from django.contrib.auth.models import User

def home(request):
    return render(request, 'support/home.html')

def tips(request):
    return render(request, 'support/tips.html')

def about(request):
    return render(request, 'support/about.html')

def assessment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        answers = [int(val) for val in data.get('answers', [])]
        results = calculate_mental_health_metrics(answers)
        return JsonResponse(results)
    return render(request, 'support/assessment.html')

def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_msg = data.get('message', '')
        bot_res = get_chat_response(user_msg)
        return JsonResponse({'response': bot_res})
    return render(request, 'support/chat.html')

def login_view(request):
    # If a user is already logged in, don't show the login page, send them to safety
    if request.user.is_authenticated:
        return redirect('/')  # Sends them to the main homepage root directly
        
    if request.method == 'POST':
        username_input = request.POST.get('username')
        password_input = request.POST.get('password')
        
        user = authenticate(request, username=username_input, password=password_input)     
        if user is not None:
            auth_login(request, user)
            return redirect('/')  # Redirects directly to root path to prevent named URL crashes!
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('/login/')
            
    return render(request, 'support/login.html')


def register_view(request):
    if request.method == 'POST':
        # 1. Get the data from the form fields using the 'name' attribute
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # 2. Simple validation check ( if username is already taken)
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'support/register.html')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'support/register.html')

        # 3. Create the user and automatically hash their password
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        # 4. Show a success message and redirect to your login page view
        messages.success(request, "Account created successfully! Please sign in.")
        return redirect('login') 

    # If it's a GET request, just display the registration page
    return render(request, 'support/register.html')


