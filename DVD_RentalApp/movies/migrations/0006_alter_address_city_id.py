# Generated by Django 4.1 on 2022-08-28 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_address_address2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.city'),
        ),
    ]