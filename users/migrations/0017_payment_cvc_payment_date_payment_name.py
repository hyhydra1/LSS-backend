# Generated by Django 4.2.5 on 2023-10-27 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_user_country_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='cvc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='date',
            field=models.DateTimeField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]