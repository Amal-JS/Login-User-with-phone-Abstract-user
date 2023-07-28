# Generated by Django 4.2.3 on 2023-07-25 10:52

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=10, validators=[user.models.CustomUser.min_length]),
        ),
    ]