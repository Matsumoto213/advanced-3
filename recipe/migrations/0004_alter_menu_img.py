# Generated by Django 3.2.7 on 2021-09-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_rename_mene_material_menu_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='img',
            field=models.ImageField(upload_to='images'),
        ),
    ]
