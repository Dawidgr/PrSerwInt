# Generated by Django 4.2.7 on 2024-01-03 16:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0002_alter_community_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='subscribed_communities', to=settings.AUTH_USER_MODEL),
        ),
    ]
