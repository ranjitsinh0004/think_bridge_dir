# Generated by Django 2.2 on 2020-05-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='choice',
            field=models.CharField(choices=[('1', 'Beverages'), ('2', 'Snacks')], default='1', max_length=20),
        ),
    ]
