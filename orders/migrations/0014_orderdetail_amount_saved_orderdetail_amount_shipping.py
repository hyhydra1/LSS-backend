# Generated by Django 4.2.5 on 2023-11-14 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_orderitem_shipping_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetail',
            name='amount_saved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='amount_shipping',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]