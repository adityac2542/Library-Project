# Generated by Django 4.0 on 2022-08-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_bookuniqueslug_requestbook_userprofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookview',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.DeleteModel(
            name='BookUniqueSlug',
        ),
    ]
