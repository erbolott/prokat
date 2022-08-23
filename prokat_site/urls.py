
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from apps.product.views import category_product , product_detail 
from apps.reviews.views import reviews
from apps.order.views import order


urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('apps.home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>', category_product , name='category_product'),
    path('product/<int:id>/<slug:slug>', product_detail, name='product_detail'),
    path('reviews/' , reviews , name='reviews'),
    path('pass/' , order , name='order'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)