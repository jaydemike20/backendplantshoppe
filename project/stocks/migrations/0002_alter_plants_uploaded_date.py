# Generated by Django 4.2.5 on 2023-09-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='uploaded_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]