# Generated by Django 4.2.5 on 2023-10-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_user_last_login_ip_user_first_signin_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
