# Generated by Django 5.0.6 on 2024-07-23 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_alter_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=8)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_outlet.address'),
        ),
    ]
