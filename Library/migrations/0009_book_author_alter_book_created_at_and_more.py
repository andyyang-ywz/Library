# Generated by Django 4.2.5 on 2023-09-30 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0008_book_stock_alter_book_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='test', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 7, 43, 53, 551660, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 30, 7, 43, 53, 552660, tzinfo=datetime.timezone.utc)),
        ),
    ]
