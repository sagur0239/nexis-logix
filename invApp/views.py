from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from authApp.forms import ProfileUpdateForm, UserUpdateForm
# Create your views here.
from .forms import ProductForm
from .models import Product
from django.views.decorators.cache import never_cache

# CRUD = Create , Read, Update, Delete
@login_required
@never_cache

# authApp/views.py ফাইলের একদম নিচে এটি আপডেট করুন
def profile_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile') # আপডেট হওয়ার পর প্রোফাইল পেজেই রিফ্রেশ হবে
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)

# Home View
@login_required
@never_cache
def home(request):
    return render(request, 'invApp/home.html')


# Create View
@login_required
@never_cache
def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})


# Read View
@login_required
@never_cache
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products':products})

# Update View
@login_required
@never_cache
def product_update_view(request, product_id):
    product = Product.objects.get(product_id=product_id)
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'invApp/product_form.html', {'form':form})

# Delete View
@login_required
@never_cache
def product_delete_view(request, product_id):
    product = Product.objects.get(product_id = product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product':product})


@login_required
@never_cache
def product_list(request):
    # আপনার আগের কোড...
    return render(request, 'invApp/product_list.html')

# ২. প্রোডাক্ট ফর্ম বা ক্রিয়েট ভিউ লক করুন 👇
@login_required
@never_cache
def product_create(request):
    # your code...
    pass