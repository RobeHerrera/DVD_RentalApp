# Generated by Django 4.1 on 2022-08-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0010_alter_customer_address_id_alter_staff_address_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='store_id',
            field=models.IntegerField(),
        ),
    ]
