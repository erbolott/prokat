from django.db import models
from django.forms import ModelForm ,TextInput , Textarea


# Create your models here.

class Reviews(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    name = models.CharField(max_length=50, null=True , verbose_name='Имя')
    email = models.CharField(max_length=200 , null=True , verbose_name='email')
    city = models.CharField(max_length=50 , null=True ,verbose_name='Город') 
    reviews = models.CharField(max_length=500, null=True , verbose_name='Отзыв')
    status = models.CharField(max_length=10, choices=STATUS, default='New', null=True) 
    create_at = models.DateTimeField(auto_now_add=True, null=True , verbose_name='Время добавления')
    update_at = models.DateTimeField(auto_now=True, null=True)
    

    def __str__(self):
        return f"{self.name} ------ {self.status}"
    
    class Meta:
        verbose_name_plural = "Отзывы"


class ReviewsForm(ModelForm):
    class Meta:
        model = Reviews
        fields = ['name', 'email', 'city' , 'reviews']

        widgets = {
            "name" : TextInput(attrs={
                'size' : "40",
                'maxlength' : '64',
                'placeholder' :'Имя, Компания'
            }),
            "email" : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' :'Телефон или электронная почта',
                'size' : "40",
            }),

            "reviews" : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' :'Ваш отзыв',
                'cols' :"60%",
                'rows' : '5'
            }),

            "city" : TextInput(attrs={
                'maxlength' : '24',
                'placeholder' :'Город',
                'size' : "40",
            }),
        }