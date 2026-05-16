from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chatbot/', views.chatbot, name="chatbot"),
    path('assessment/', views.assessment, name='assessment'), 
    path('tips/', views.trip, name='tips'),
    path('about/', views.about, name='about'),
    
]