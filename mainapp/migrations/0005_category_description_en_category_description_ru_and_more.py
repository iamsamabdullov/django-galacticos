# Generated by Django 4.2.4 on 2024-08-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_filterplayersview'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='players',
            name='country_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='players',
            name='country_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='players',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='players',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='players',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='players',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='players',
            name='tagline_en',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Прозвище'),
        ),
        migrations.AddField(
            model_name='players',
            name='tagline_ru',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='Прозвище'),
        ),
    ]
