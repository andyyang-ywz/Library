# Generated by Django 4.2.5 on 2023-09-30 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0011_alter_book_created_at_alter_transaction_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 14, 48, 17, 940586, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 14, 48, 17, 941587, tzinfo=datetime.timezone.utc)),
        ),
    ]
