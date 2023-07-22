# Generated by Django 4.2.3 on 2023-07-22 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(help_text='Order Date')),
                ('region', models.CharField(help_text='Region', max_length=50)),
                ('city', models.CharField(help_text='City', max_length=50)),
                ('category', models.CharField(help_text='Category', max_length=50)),
                ('product', models.CharField(help_text='Product', max_length=50)),
                ('quantity', models.DecimalField(decimal_places=2, help_text='Quantity', max_digits=18)),
                ('unit_price', models.DecimalField(decimal_places=2, help_text='Unit Price', max_digits=18)),
            ],
        ),
    ]