from re import template
from django.shortcuts import render
from apps.home.models import Setting
from .models import Category,Product , Images ,ProductFilter
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.db.models import Q


# Create your views here.

def category_product(request,id , slug):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    catdata = Category.objects.get(pk = id)
    product = Product.objects.filter(category_id = id)
    paginator = Paginator(product , 2) 
    page_number=request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    product_size = Product.objects.filter(category_id = id).order_by('size')

    min_price = request.GET.get('min-price')
    max_price = request.GET.get('max-price')


    sort_by = request.GET.get("sort", "default") 
            
    if sort_by == "price_ascending":
            products_sort = Product.objects.all().order_by("price")
    elif sort_by == "price-desc":
            products_sort = Product.objects.all().order_by("-price")
    elif sort_by == "name_ascending":
            products_sort = Product.objects.all().order_by("title")
    elif sort_by == "default":
            products_sort = paginator.get_page(page_number)

    queryset = Product.objects.filter(
        Q(size__in =request.GET.getlist("size"))|
        Q(price__range=(min_price, max_price))
    )


    context = {
        'settings' : settings,
        'category' : category,
        'product' : product,
        'catdata' : catdata,
        'products_sort' : products_sort,
        'product_size' : product_size,
        'queryset' : queryset, 
        'page_obj' : page_obj
    }
    return render(request , 'category_products.html' , context)
   



def product_detail(request, id , slug):
    settings = Setting.objects.get(pk=1)
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    images = Images.objects.filter(product_id=id)
    similar_products = Product.objects.filter(category_id=id)
    context = {
        'settings':settings,
        'category':category,
        'product':product,
        'images': images,
        'similar_products' : similar_products,
    }
    return render(request , 'product_detail.html' , context)

