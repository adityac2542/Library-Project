# Generated by Django 4.0 on 2022-08-28 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_userprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]
