# Generated by Django 4.0.1 on 2022-02-01 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='create_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Время добавления'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='update_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]