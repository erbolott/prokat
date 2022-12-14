# Generated by Django 4.0.1 on 2022-01-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Заголовок')),
                ('img', models.ImageField(null=True, upload_to='news_images/', verbose_name='Фото')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='дата публикации')),
            ],
        ),
    ]
