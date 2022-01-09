# Generated by Django 4.0 on 2021-12-19 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255)),
                ('info', models.TextField()),
                ('date', models.DateTimeField()),
                ('cost', models.IntegerField(default=0)),
                ('picture', models.ImageField(default='donut-default.jpg', upload_to='donuts/')),
            ],
            options={
                'verbose_name': 'Пончик',
                'verbose_name_plural': 'Пончики',
            },
        ),
    ]