# Generated by Django 4.0 on 2022-08-22 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('library', '0003_libusercreation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookUniqueSlug',
            fields=[
                ('bookview_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.bookview')),
            ],
            bases=('library.bookview',),
        ),
        migrations.CreateModel(
            name='RequestBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_req', models.BooleanField(default=False)),
                ('bookname', models.CharField(max_length=100)),
                ('issue_status', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=200)),
                ('usr_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_related', to='auth.user')),
            ],
        ),
        migrations.DeleteModel(
            name='LibUserCreation',
        ),
        migrations.AddField(
            model_name='bookview',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='bookview',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.CreateModel(
            name='UsrBookReqOrders',
            fields=[
                ('requestbook_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='library.requestbook')),
                ('books_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.bookview')),
                ('usr_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
            bases=('library.requestbook',),
        ),
    ]
