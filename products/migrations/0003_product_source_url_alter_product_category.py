# Generated by Django 4.2.5 on 2023-10-17 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_published_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='source_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category'),
        ),
    ]