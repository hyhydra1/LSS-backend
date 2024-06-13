# Generated by Django 4.2.5 on 2023-11-16 12:57

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_inquiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]
