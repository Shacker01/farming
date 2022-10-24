# Generated by Django 4.1.2 on 2022-10-17 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Animal_name', models.CharField(max_length=20)),
                ('update', models.DateField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Img', models.ImageField(upload_to='')),
                ('Description', models.TextField()),
                ('Price_Ksh', models.IntegerField()),
                ('Offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=10)),
                ('disease_image', models.ImageField(upload_to='')),
                ('describe', models.TextField(max_length=200)),
            ],
        ),
    ]
