# Generated by Django 4.1.7 on 2023-03-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
