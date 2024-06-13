# Generated by Django 4.2.5 on 2023-11-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_remove_shipping_global_rate_remove_shipping_usa_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='dimension',
        ),
        migrations.AddField(
            model_name='shipping',
            name='dimension_h',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='dimension_l',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='shipping',
            name='dimension_w',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]