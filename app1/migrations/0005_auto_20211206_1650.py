# Generated by Django 3.2.5 on 2021-12-06 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_signup_repassword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='your_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='destination',
            old_name='your_name',
            new_name='username',
        ),
    ]
