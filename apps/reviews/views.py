from django.shortcuts import render

from apps.product.models import Category
from .models import Reviews,ReviewsForm
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from apps.home.models import Setting

# Create your views here.

def reviews(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
           data = Reviews()
           data.name = form.cleaned_data['name']
           data.email = form.cleaned_data['email']
           data.city = form.cleaned_data['city']
           data.reviews = form.cleaned_data['reviews']
           data.save()
           messages.success(request, "Спасибо за ваш отзыв!")
        else:
            messages.warning(request, 'Форма была неверной')
            return HttpResponseRedirect('/reviews')

    form = ReviewsForm()
    settings = Setting.objects.get(pk=1)
    reviews = Reviews.objects.filter(status='True')
    category = Category.objects.all()
    context = {
        'settings' : settings,
        'form' : form,
        'reviews' : reviews,
        'category' : category
    }
    return render(request , 'reviews.html' , context)