# Generated by Django 4.0 on 2021-12-19 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_operatingsystem_publication_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computer',
            name='photo',
            field=models.ImageField(default='default-computer.jpg', upload_to=''),
        ),
    ]
