# Generated by Django 4.2.4 on 2024-08-23 11:54

from django.db import migrations, models
import django.db.models.deletion
import django.views.generic.list


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_players_draft'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterPlayersView',
            fields=[
                ('category_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.category')),
            ],
            bases=('mainapp.category', django.views.generic.list.ListView),
        ),
    ]
