# Generated by Django 5.0.6 on 2024-07-15 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_stockdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockdata',
            name='close',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='high',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='low',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='stockdata',
            name='open',
            field=models.CharField(max_length=20),
        ),
    ]