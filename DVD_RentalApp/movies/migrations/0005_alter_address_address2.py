# Generated by Django 4.1 on 2022-08-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_address_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address2',
            field=models.CharField(max_length=255, null=True),
        ),
    ]