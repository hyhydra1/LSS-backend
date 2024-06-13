# Generated by Django 4.2.5 on 2023-11-02 21:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_user_otp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('sponsored_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='sponsor_user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_active', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('order_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='sponsor_order_payments', to='users.payment')),
                ('sponsor_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsored_users', to=settings.AUTH_USER_MODEL)),
                ('subscription_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='sponsor_subscription_payments', to='users.payment')),
            ],
            options={
                'verbose_name': 'Sponsor Model',
                'ordering': ['-created_at'],
            },
        ),
    ]