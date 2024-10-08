# Generated by Django 4.2.4 on 2024-04-01 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('number', models.IntegerField(max_length=100, verbose_name='Номер')),
                ('position', models.CharField(max_length=100, verbose_name='Амплуа')),
                ('games', models.IntegerField(max_length=100, verbose_name='Игры')),
                ('goals', models.IntegerField(max_length=100, verbose_name='Голы')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Прозвище')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster', models.ImageField(upload_to='players/', verbose_name='Постер')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Дата рождения')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('datas', models.CharField(max_length=30, verbose_name='Годы выступления')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Игрок',
                'verbose_name_plural': 'Игроки',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звезды рейтинга',
                'ordering': ['-value'],
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.reviews', verbose_name='Родитель')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.players', verbose_name='игрок')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='mainapp.players', verbose_name='игрок')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ratingstar', verbose_name='звезда')),
            ],
            options={
                'verbose_name': 'Рейтинг',
                'verbose_name_plural': 'Рейтинги',
            },
        ),
        migrations.CreateModel(
            name='PlayersShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='players_shots/', verbose_name='Изображение')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.players', verbose_name='Игрок')),
            ],
            options={
                'verbose_name': 'Фото игрока',
                'verbose_name_plural': 'Фото игрока',
            },
        ),
    ]
