
# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .utils import calculate_mental_health_metrics, get_chat_response
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


