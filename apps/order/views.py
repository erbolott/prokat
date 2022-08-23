from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect

from apps.product.models import Category
from .models import Order , OrderForm
from apps.home.models import Setting
# Create your views here.


def order(request):
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
           messages.success(request, "Спасибо за ваш отзыв!")
        else:
            messages.warning(request, 'Форма была неверной')
            return HttpResponseRedirect('/pass')

    form = OrderForm()
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        'settings' : settings,
        'form' : form,
        'category' : category
    }
    return render(request , 'pass.html' , context)
