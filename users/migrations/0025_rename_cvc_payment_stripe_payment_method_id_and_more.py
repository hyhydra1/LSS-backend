# Generated by Django 4.2.5 on 2023-11-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0024_sponsor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='cvc',
            new_name='stripe_payment_method_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='date',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='method',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='name',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='provider',
        ),
        migrations.AddField(
            model_name='user',
            name='stripe_customer_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
