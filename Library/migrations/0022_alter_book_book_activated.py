# Generated by Django 4.2.5 on 2023-10-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0021_book_book_activated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_activated',
            field=models.BooleanField(default=0),
        ),
    ]