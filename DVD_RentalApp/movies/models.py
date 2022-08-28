from django.db import models
from django.utils import timezone


class Genre(models.Model):
    """
    Describe the model of Genre use for the Data Base
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    """ 
    Describe the model of Movie use for the Data Base
    """
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stocks = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_created = models.DateField(default=timezone.now)

class Actor(models.Model):
    """ 
    Describe the model of Actor use for the Data Base
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)

class Address(models.Model):
    """ 
    Describe the model of Address use for the Data Base
    """
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null = True)
    district = models.CharField(max_length=255)
    city_id = models.IntegerField()
    postal_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)

    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Addresses"

class Category(models.Model):
    """ 
    Describe the model of Category use for the Data Base
    """
    name = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Categories"

class City(models.Model):
    """ 
    Describe the model of City use for the Data Base
    """
    city = models.CharField(max_length=255)
    country_id = models.IntegerField()
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Cities"

class Country(models.Model):
    """ 
    Describe the model of Country use for the Data Base
    """
    country = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Countries"

class Customer(models.Model):
    """ 
    Describe the model of Customer use for the Data Base
    """
    store_id = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address_id = models.IntegerField()
    activebool = models.BooleanField()
    create_date = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    active = models.IntegerField()

# class FilmActor(models.Model):
#     """ 
#     Describe the model of FilmActor use for the Data Base
#     """
#     film_id = models.IntegerField()
#     last_update = models.CharField(max_length=255)

class FilmCategory(models.Model):
    """ 
    Describe the model of FilmCategory use for the Data Base
    """
    film_id = models.IntegerField()
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "FilmCategories"

class Film(models.Model):
    """ 
    Describe the model of Film use for the Data Base
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_year = models.IntegerField()
    language_id = models.IntegerField()
    rental_duration = models.IntegerField()
    rental_rate = models.FloatField()
    length = models.IntegerField()
    replacement_cost = models.FloatField()
    rating = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    special_features = models.CharField(max_length=255)
    fulltext = models.CharField(max_length=255)

class Inventory(models.Model):
    """ 
    Describe the model of Inventory use for the Data Base
    """
    film_id = models.IntegerField()
    store_id = models.IntegerField()
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Inventories"

class Language(models.Model):
    """ 
    Describe the model of Language use for the Data Base
    """
    name = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)

class Payment(models.Model):
    """ 
    Describe the model of Payment use for the Data Base
    """
    customer_id = models.IntegerField()
    staff_id = models.IntegerField()
    rental_id = models.IntegerField()
    amount = models.FloatField()
    payment_date = models.CharField(max_length=255)

class Rental(models.Model):
    """ 
    Describe the model of Rental use for the Data Base
    """
    rental_date = models.CharField(max_length=255)
    inventory_id = models.IntegerField()
    customer_id = models.IntegerField()
    return_date = models.CharField(max_length=255)
    staff_id = models.IntegerField()
    last_update = models.CharField(max_length=255)

class Staff(models.Model):
    """ 
    Describe the model of Staff use for the Data Base
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address_id = models.IntegerField()
    email = models.CharField(max_length=255)
    store_id = models.IntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    picture = models.CharField(max_length=255, null = True)

class Store(models.Model):
    """ 
    Describe the model of Store use for the Data Base
    """
    manager_staff_id = models.IntegerField()
    address_id = models.IntegerField()
    last_update = models.CharField(max_length=255)