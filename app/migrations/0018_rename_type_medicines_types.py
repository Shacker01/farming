# Generated by Django 4.1.3 on 2022-11-13 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_medicines'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicines',
            old_name='type',
            new_name='types',
        ),
    ]
