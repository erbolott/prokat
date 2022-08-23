# Generated by Django 4.0.1 on 2022-02-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_news_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slier_promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='slider_promotion/', verbose_name='Картинка')),
                ('create_at', models.DateField(auto_now_add=True, null=True, verbose_name='дата публикации')),
            ],
            options={
                'verbose_name_plural': 'Слайдер акций',
            },
        ),
    ]