# Generated by Django 4.2.5 on 2023-11-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_remove_orderdetail_stripe_invoice_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='shipping_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]