"""
URL configuration for invProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ১. কেউ শুধু মেইন লিংকে ঢুকলে (যেমন: http://127.0.0.1:8000/) সরাসরি লগইন পেজে নিয়ে যাবে
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # ২. অ্যাডমিন প্যানেল রুট (আগের মতোই থাকবে)
    path('admin/', admin.site.urls),
    
    # ৩. আপনার ইনভেন্টরি অ্যাপের ইউআরএল লিংক (যা আগে মেইন রুটে ছিল, এখন সেটিও সচল থাকবে)
    path('inv/', include('invApp.urls')),
    
    # ৪. অথেনটিকেশন বা প্রোফাইল অ্যাপের ইউআরএল লিংক
    path('auth/', include("authApp.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)