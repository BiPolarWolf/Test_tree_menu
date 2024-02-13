# Generated by Django 4.0 on 2024-02-13 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Название меню')),
                ('description', models.CharField(blank=True, max_length=300, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Название пункта меню')),
                ('description', models.TextField(blank=True, max_length=300, verbose_name='Описание')),
                ('url', models.CharField(blank=True, help_text='Указывается для перехода на ресурс из конечного пункта меню, если не указать, то алгоритм будет пытаться найти потомков данного пункта меню и создать из них подменю', max_length=50, verbose_name='URL-адрес стороннего ресурса')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='app.menu')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.menuitem')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Пункты меню',
                'ordering': ['id'],
            },
        ),
    ]
