# Generated by Django 4.0.1 on 2022-02-01 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_news_options_news_detail_news_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]