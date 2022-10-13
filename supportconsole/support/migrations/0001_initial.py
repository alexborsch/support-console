# Generated by Django 4.1.2 on 2022-10-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupportCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Компанія')),
                ('start_date', models.DateTimeField(verbose_name='Дата початок')),
                ('end_date', models.DateTimeField(verbose_name='Дата кінець')),
                ('status', models.BooleanField(verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'компанія',
                'verbose_name_plural': 'компанії',
            },
        ),
        migrations.CreateModel(
            name='SupportPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Преорітет')),
            ],
            options={
                'verbose_name': 'преорітет',
                'verbose_name_plural': 'преорітети',
            },
        ),
        migrations.CreateModel(
            name='SupportStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'статус тікета',
                'verbose_name_plural': 'статус тікета',
            },
        ),
    ]
