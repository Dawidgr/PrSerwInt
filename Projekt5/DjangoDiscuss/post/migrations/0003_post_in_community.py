# Generated by Django 4.2.7 on 2024-01-03 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_community_members'),
        ('post', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='in_community',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.community'),
        ),
    ]