# To handle views and redirects
from django.shortcuts import render, redirect
# To Import auth functions form Django
from django.contrib.auth import authenticate, login, logout
# The login_required decorator to protect views
from django.contrib.auth.decorators import login_required
# For class-based views[CBV]
from django.contrib.auth.mixins import LoginRequiredMixin
# For class-based views[CBV]
from django.views import View
# Import the User class (model)
from django.contrib.auth.models import User
# Import the RegisterForm from forms.py
from .forms import RegisterForm, LoginForm
from .forms import UserUpdateForm, ProfileUpdateForm


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error_message = None 
    # ব্রাউজার ইউআরএল থেকে 'next' প্যারামিটারটি নেওয়া হচ্ছে (যদি কোনো পেজ থেকে রিডাইরেক্ট হয়ে আসে)
    next_url = request.GET.get('next', '')
    
    if request.method == "POST": 
        form = LoginForm(request.POST)
        # ফর্ম সাবমিট হওয়ার পর যদি 'next' এর মান থাকে তবে সেখানে যাবে, না থাকলে সরাসরি ইনভেন্টরি 'home'-এ যাবে
        next_url = request.POST.get('next') or 'home'
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password") 
            user = authenticate(request, username=username, password=password)  
            
            if user is not None:  
                login(request, user)  
                # সমাধান: এখানে আগে '/auth/' হার্ডকোড করা ছিল, যা পরিবর্তন করে dynamic next_url বা 'home' করা হলো
                if next_url and next_url != 'home':
                    return redirect(next_url)
                return redirect('home')
            else:
                error_message = "Invalid credentials"  
    else:
        form = LoginForm()
        
    return render(request, 'accounts/login.html', {'form': form, 'error': error_message, 'next': next_url})

    
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')


# Home View (Inventory Main Dashboard)
@login_required
def home_view(request):
    # সমাধান: টেমপ্লেট পাথটি আপনার ইনভেন্টরি অ্যাপের স্ট্রাকচার অনুযায়ী 'invApp/home.html' হওয়া উচিত
    return render(request, 'invApp/home.html')


# Protected View 
class ProtectedView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'registration/protected.html')
    
@login_required
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)