# Generated by Django 4.2.5 on 2023-11-25 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_alter_address_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]