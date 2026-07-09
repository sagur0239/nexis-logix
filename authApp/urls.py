from django.urls import path
from . import views

urlpatterns = [
    # রেজিস্ট্রেশন এবং লগইন ইউআরএল
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    
    # লগআউট ইউআরএল (নিশ্চিত করুন name='logout' দেওয়া আছে)
    path('logout/', views.logout_view, name='logout'),
    
    # প্রোফাইল ইউআরএল (নিশ্চিত করুন name='profile' দেওয়া আছে)
    path('profile/', views.profile_view, name='profile'),
    
    # প্রটেক্টেড ভিউ (যদি আপনার প্রজেক্টে থেকে থাকে)
    path('protected/', views.ProtectedView.as_view(), name='protected'),
]