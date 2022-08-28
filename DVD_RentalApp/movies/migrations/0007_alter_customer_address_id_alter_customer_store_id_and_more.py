# Generated by Django 4.1 on 2022-08-28 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_address_city_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.address'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.store'),
        ),
        migrations.AlterField(
            model_name='film',
            name='language_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.language'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='film_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.film'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.store'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.customer'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='rental_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.rental'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='staff_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.staff'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.address'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='store_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.store'),
        ),
        migrations.AlterField(
            model_name='store',
            name='address_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.address'),
        ),
    ]
