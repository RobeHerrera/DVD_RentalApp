# Generated by Django 4.1 on 2022-08-28 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_category_city_country_customer_film_filmcategory_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'Cities'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='filmcategory',
            options={'verbose_name_plural': 'FilmCategories'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': 'Inventories'},
        ),
        migrations.AlterField(
            model_name='staff',
            name='picture',
            field=models.CharField(max_length=255, null=True),
        ),
    ]