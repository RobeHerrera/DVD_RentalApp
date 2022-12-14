# Generated by Django 4.1 on 2022-08-28 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_customer_address_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.address'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_address', to='movies.address'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_store', to='movies.store'),
        ),
    ]
