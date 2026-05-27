from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('chatbot/', views.chatbot, name="chatbot"),
    path('assessment/', views.assessment, name='assessment'), 
    path('tips/', views.tips, name='tips'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
]