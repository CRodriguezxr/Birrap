# Generated by Django 4.0.6 on 2022-08-27 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cervezas', '0002_category_cerveza_delete_black_delete_blonde_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='style',
        ),
    ]