# Generated by Django 4.2.5 on 2023-11-01 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_alter_user_auth_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='otp',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]