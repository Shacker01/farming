# Generated by Django 2.2.26 on 2022-09-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=200)),
                ('Last_name', models.CharField(max_length=200)),
                ('Username', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=30)),
                ('psswod2', models.CharField(max_length=30)),
            ],
        ),
    ]
