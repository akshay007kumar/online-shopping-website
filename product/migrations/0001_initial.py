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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=40)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_desctiption', models.TextField()),
                ('quantity_per_unit', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('picture', models.ImageField(default='default.png', upload_to='product/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Category')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.SubCategory')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Supplier')),
            ],
        ),
    ]