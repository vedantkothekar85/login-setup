# Generated by Django 4.1 on 2023-01-17 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_shell', '0004_try_new_alter_new_signup_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_signup',
            name='dob',
            field=models.DateField(default=datetime.datetime(2023, 1, 17, 20, 18, 26, 89379)),
        ),
    ]
