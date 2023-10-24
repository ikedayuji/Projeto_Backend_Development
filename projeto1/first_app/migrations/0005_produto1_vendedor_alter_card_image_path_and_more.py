# Generated by Django 4.2.4 on 2023-10-24 18:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0004_card_grafico'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='image_path',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('data', models.DateTimeField(default=datetime.datetime(2023, 10, 24, 15, 24, 12, 806032))),
                ('nome_produto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='first_app.produto1')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='first_app.vendedor')),
            ],
        ),
    ]
