# Generated by Django 3.2.16 on 2024-09-12 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_follow_unique_name_owner'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_name_owner',
        ),
    ]
