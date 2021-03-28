# Generated by Django 3.1.7 on 2021-03-28 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='pictures/')),
                ('availability', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available'), ('Archived', 'Archived'), ('Out of stock', 'Out of stock')], default='Available', max_length=13)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.category')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.producttype')),
            ],
        ),
    ]