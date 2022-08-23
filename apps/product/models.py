from tkinter.tix import Form
from xmlrpc.client import MAXINT
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
import django_filters
from django.forms import CheckboxInput

# Create your models here.

class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True , verbose_name='название категории' , null=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    keywords = models.CharField(max_length=255 , verbose_name='ключевые слова' , null=True)
    image = models.ImageField(upload_to ='category' , verbose_name='фото' , null=True)
    description = models.TextField(verbose_name='Описание' , null=True)
    slug = models.SlugField(null=True , unique=True)
    create_at = models.DateTimeField(auto_now_add= True , verbose_name='время создания' , null=True)
    upload_at = models.DateTimeField(auto_now= True , verbose_name='время изменения' , null=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return ' / '.join(full_path[::-1])

    class Meta:
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse("category_detail" , kwargs={'slug' : self.slug }) # для создания ссылки на отдельную страницу категории

    def get_absolute_url(self):
        return reverse("category_detail" , kwargs={'slug' : self.slug })

class Product(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE, verbose_name='категория' , null=True)
    title = models.CharField(max_length=100 , verbose_name='Название товара' ,null=True)
    keywords = models.CharField(max_length=255 , verbose_name='ключевые словa' , null=True)
    image = models.ImageField(upload_to ='image_product' , verbose_name='фото' , null=True)
    price = models.IntegerField(verbose_name='Цена' , null=True)
    description = models.TextField(verbose_name='Описание товара' , null=True)
    detail = RichTextUploadingField(null=True)
    slug = models.SlugField(null=True)
    create_at = models.DateTimeField(auto_now_add= True , verbose_name='время публикации' , null=True)
    upload_at = models.DateTimeField(auto_now= True , verbose_name='время изменения' , null=True)
    size = models.IntegerField(verbose_name='Размер:' , null=True)

    def __str__(self):
        return self.title or ''

    class Meta:
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse("product_detail" , kwargs={'slug' : self.slug })

    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="80px">'.format(self.image.url))
    image_tag.short_description = 'Фото'



class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ['size']



class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/" , verbose_name='дополнительные картинки')

    def __str__(self):
        return f"id: {self.id} -------- товар: {self.product}"
    
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="80px">'.format(self.image.url))
    image_tag.short_description = 'Фото'
    
    class Meta:
        verbose_name_plural = "Картинки"