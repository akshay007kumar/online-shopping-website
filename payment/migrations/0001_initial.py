# Generated by Django 2.2.2 on 2019-06-05 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('order_number', models.IntegerField(unique=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Customer')),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Shipper')),
            ],
        ),
    ]