# Generated by Django 4.2.5 on 2023-10-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0002_seller_account_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='phone_number',
            field=models.CharField(default=123, max_length=12),
            preserve_default=False,
        ),
    ]