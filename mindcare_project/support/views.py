
# Create your views here.
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .utils import calculate_mental_health_metrics, get_chat_response
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
import json

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


