# Generated by Django 4.1.7 on 2023-03-29 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_alter_follows_follower_alter_follows_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follows',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
