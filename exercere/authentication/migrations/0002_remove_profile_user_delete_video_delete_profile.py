# Generated by Django 5.0.6 on 2024-05-24 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Video',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
