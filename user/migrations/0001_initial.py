# Generated by Django 2.2.2 on 2019-06-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('status', models.CharField(default='Active', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='First Name', max_length=12)),
                ('last_name', models.CharField(default='Last Name', max_length=12)),
                ('permanent_address', models.TextField(default='Permanent Address')),
                ('shipping_address', models.TextField(default='Shipping Address')),
                ('profile_image', models.ImageField(default='default.png', upload_to='profile')),
                ('bio', models.TextField(default='Your Bio')),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('dob', models.DateField(default='1990-01-01')),
                ('profile_status', models.CharField(max_length=20, verbose_name='Activate')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.Customer')),
            ],
        ),
    ]
