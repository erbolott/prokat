from django.db import models
from django.forms import ModelForm ,TextInput , Textarea , DateInput

# Create your models here.

class Order(models.Model):
    date = models.DateField(null=True, verbose_name='Дата примера')
    phone = models.CharField(max_length=20 , null=True , verbose_name='Телефон')
    first_name = models.CharField(max_length=50 , null=True , verbose_name='Имя')
    last_name = models.CharField(max_length=50 , null=True , verbose_name='Фамилия')
    message = models.TextField(null=True , verbose_name='Сообщение')
    send_time = models.DateTimeField(null=True , verbose_name='Время отправки' , auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} ------ {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Записи на пропуск"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'phone', 'first_name' , 'last_name' , 'message']

        widgets = {
            "date" : DateInput(attrs={
                'class' : 'flatpickr flatpickr-input',
                'placeholder' :'Выберите день',
            }),
            "phone" : TextInput(attrs={
                # 'placeholder' :'Телефон или электронная почта',
                # 'size' : "40",
                # 'type':'tel',
                # 'id' : 'phone',
                # 'placeholder':'+996 (___) ___-__-__',
                'autocomplete':'off'
            }),

            "message" : Textarea(attrs={
                'placeholder' :'Ваши комментарии и пожелания',
            }),

            "first_name" : TextInput(attrs={
                'placeholder' :'Имя',
                'class' : 'fio'
            }),

             "last_name" : TextInput(attrs={
                'placeholder' :'Фамилия',
                'class' : 'fio'
            }),

        }