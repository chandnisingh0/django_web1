# Generated by Django 3.2.5 on 2021-12-05 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('passwordd', models.TextField()),
                ('repassword', models.TextField()),
            ],
        ),
    ]
