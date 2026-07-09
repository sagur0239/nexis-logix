from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from invApp.forms import ProductForm
from invApp.models import Product

# ==============================================================================
# ১. প্রোডাক্ট লিস্ট ভিউ (সুরক্ষিত এবং ক্যাশ লক করা)
# ==============================================================================
@method_decorator(never_cache, name='dispatch')
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'invApp/product_list.html'
    context_object_name = 'products'  # আপনার টেমপ্লেটে {% for product in products %} এর জন্য


# ==============================================================================
# ২. প্রোডাক্ট ক্রিয়েট ভিউ (সুরক্ষিত)
# ==============================================================================
class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'invApp/product_form.html'
    success_url = reverse_lazy('product_list') 


# ==============================================================================
# ৩. প্রোডাক্ট আপডেট ভিউ (সুরক্ষিত)
# ==============================================================================
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'invApp/product_form.html'
    success_url = reverse_lazy('product_list')


# ==============================================================================
# ৪. প্রোডাক্ট ডিলিট ভিউ (সুরক্ষিত)
# ==============================================================================
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'invApp/product_confirm_delete.html'  # আপনার ডিলিট কনফার্মেশন ফাইল নাম অনুযায়ী দেখে নেবেন
    success_url = reverse_lazy('product_list')vv