# Generated by Django 4.0.6 on 2022-09-01 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comidas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comidas',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
