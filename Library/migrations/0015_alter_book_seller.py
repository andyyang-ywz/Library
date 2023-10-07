# Generated by Django 4.2.5 on 2023-10-07 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0002_seller_account_active'),
        ('Library', '0014_book_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='seller',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Seller.seller'),
        ),
    ]