# Generated by Django 3.2 on 2021-05-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_rename_date_field_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
