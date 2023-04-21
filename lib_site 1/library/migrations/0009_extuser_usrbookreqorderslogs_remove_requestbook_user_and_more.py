# Generated by Django 4.0 on 2022-09-07 08:00

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_alter_user_email'),
        ('library', '0008_alter_userprofile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UsrBookReqOrdersLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='requestbook',
            name='user',
        ),
        migrations.AddField(
            model_name='requestbook',
            name='author',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='requestbook',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookview',
            name='author_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bookview',
            name='book_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='requestbook',
            name='bookname',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.DeleteModel(
            name='UsrBookReqOrders',
        ),
        migrations.AddField(
            model_name='requestbook',
            name='user_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.usrbookreqorderslogs'),
        ),
    ]
