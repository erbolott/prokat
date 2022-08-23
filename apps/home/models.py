
from email.mime import image
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100 , verbose_name='Название сайта' , null=True)
    logo = models.ImageField(upload_to='logo' , verbose_name='Логотип' , null=True)
    keywords = models.CharField(max_length=200 , verbose_name='Ключевые слова' , null=True)
    description = models.TextField(verbose_name='Описание сайта', null=True)

    # контакты 
    location = models.CharField(max_length=100 , verbose_name='Локация' , help_text='Мы находимся по адресу ул.Ленина 232', null=True, blank=True )
    phone = models.CharField(max_length=100 , verbose_name='Телефон' , blank=True , null=True)
    email = models.CharField(max_length=30 , verbose_name='email' , blank=True , null=True)
    time_work = models.CharField(max_length=200 , verbose_name='Время работы' , blank=True , null=True)

    # социальные сети
    telegram = models.CharField(max_length=200 , verbose_name='telegram' , blank=True , null=True)
    watsapp = models.CharField(max_length=200 , verbose_name='watsapp' , blank=True , null=True)
    instagram = models.CharField(max_length=200 , verbose_name='instagram' , blank=True , null=True)
    

    # about_page = RichTextUploadingField(null=True ,  blank=True )



    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Основные настройки'


class News(models.Model):
    title = models.CharField(max_length=200 , null=True , verbose_name='Заголовок')
    img = models.ImageField(upload_to = "news_images/" ,null=True , verbose_name='Фото')
    description = models.CharField(max_length=100,null=True , verbose_name='Кароткое описание')
    create_at = models.DateField(null=True , auto_now_add=True , verbose_name='дата публикации')

    def __str__(self):
        return f"{self.title} | опубликовано {self.create_at}"

    class Meta:
        verbose_name_plural = 'Новости'



class Slier_promotion(models.Model):
    image1 = models.ImageField(upload_to="slider_promotion/" ,null=True , verbose_name='Картинка')
    image2 = models.ImageField(upload_to="slider_promotion/" ,null=True , verbose_name='Картинка')
    image3 = models.ImageField(upload_to="slider_promotion/" ,null=True , verbose_name='Картинка')
    image4 = models.ImageField(upload_to="slider_promotion/" ,null=True , verbose_name='Картинка')
    create_at = models.DateField(null=True , auto_now_add=True , verbose_name='дата публикации')

    def __str__(self):
        return f"{self.id} | опубликовано {self.create_at}"

    class Meta:
        verbose_name_plural = 'Слайдер акций'

    # def image_tag(self):
    #     if self.image.url is not None:
    #         return mark_safe('<img src="{}" height="80px">'.format(self.image.url))
    # image_tag.short_description = 'Фото'
