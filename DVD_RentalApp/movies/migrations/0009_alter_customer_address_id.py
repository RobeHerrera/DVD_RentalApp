# Generated by Django 4.1 on 2022-08-28 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_filmcategory_film_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='movies.address'),
        ),
    ]