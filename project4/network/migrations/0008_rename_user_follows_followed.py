# Generated by Django 4.1.7 on 2023-03-30 21:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0007_alter_follows_follower"),
    ]

    operations = [
        migrations.RenameField(
            model_name="follows",
            old_name="user",
            new_name="followed",
        ),
    ]