from django.shortcuts import render
from .models import Setting , News , Slier_promotion
from apps.product.models import Category , Product
from apps.reviews.models import Reviews
from django.http.response import HttpResponseRedirect
from .forms import SearchForm
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.contrib import messages
from apps.order.models import Order , OrderForm


# Create your views here.

def Home(request):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    reviews = Reviews.objects.filter(status='True').order_by('-create_at')
    news = News.objects.all().order_by('-create_at')[:3]
    novinki_product = Product.objects.all().order_by('-create_at')
    slier_promotion = Slier_promotion.objects.get(pk=3)
    context={
        'settings' : settings,
        'category' : category,
        'reviews' : reviews,
        'news' : news,
        'novinki_product' : novinki_product,
        'slier_promotion' : slier_promotion
    }
    return render(request , 'index.html' , context)




def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__iregex=query)
            
            category = Category.objects.all()
            settings = Setting.objects.get(pk=1)
            paginator = Paginator(products , 20) 

            page_number=request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context = {
                'products':products,
                'query':query,
                'category':category,
                'settings':settings,
                'page_obj' : page_obj
            }
            return render(request, 'search_products.html', context)
        return HttpResponseRedirect('/')


def news(request):
    settings = Setting.objects.get(pk=1)
    news = News.objects.all().order_by('-id')
    paginator = Paginator(news , 2)
    category = Category.objects.all()
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'settings' : settings,
        'news' : news,
        'page_obj' : page_obj,
        'category' : category
    }
    return render(request , 'news.html' , context)


def contact_page(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
           data = Order()
           data.phone = form.cleaned_data['phone']
           data.first_name = form.cleaned_data['first_name']
           data.last_name = form.cleaned_data['last_name']
           data.message = form.cleaned_data['message']
           data.date = form.cleaned_data['date']
           data.save()
           messages.success(request, "Спасибо, что написали нам! Мы скоро свяжемся с вами.")
           return HttpResponseRedirect('/contact/#Spasibo')
        else:
            messages.warning(request, 'Форма была неверной')
            return HttpResponseRedirect('/contact')

    form = OrderForm()
    category = Category.objects.all()
    settings = Setting.objects.get(pk=1)
    context={
      'settings' : settings ,
      'form' : form,
      'category' : category
    }
    return render(request , 'contact.html' , context)


def uslovia_page(request):
    category = Category.objects.all()
    settings = Setting.objects.get(pk=1)
    context = {
        'settings' : settings,
        'category' : category
    }
    return render(request , 'uslovia.html' , context)

def tablitsa_razmerov(request):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'settings' : settings,
        'category' : category
    }
    return render(request , 'tablitsa_razmerov.html' , context)