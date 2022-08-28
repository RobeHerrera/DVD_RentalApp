from django.db import models
from django.utils import timezone


############################## Simple Test Database #################################   

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

############################## Actual Database #################################    

class Actor(models.Model):
    """ 
    Describe the model of Actor use for the Data Base
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)

class City(models.Model):
    """ 
    Describe the model of City use for the Data Base
    """
    city = models.CharField(max_length=255)
    country = models.IntegerField()
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Cities"
    def __str__(self):
        return self.city

class Address(models.Model):
    """ 
    Describe the model of Address use for the Data Base
    """
    address = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, null = True)
    district = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)

    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Addresses"

    def __str__(self):
        return str(self.address)

class Category(models.Model):
    """ 
    Describe the model of Category use for the Data Base
    """
    name = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Categories"

class Country(models.Model):
    """ 
    Describe the model of Country use for the Data Base
    """
    country = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Countries"

class FilmActor(models.Model):
    """ 
    Describe the model of FilmActor use for the Data Base
    """
    film = models.IntegerField()
    last_update = models.CharField(max_length=255)


class Language(models.Model):
    """ 
    Describe the model of Language use for the Data Base
    """
    name = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Film(models.Model):
    """ 
    Describe the model of Film use for the Data Base
    """
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    release_year = models.IntegerField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    rental_duration = models.IntegerField()
    rental_rate = models.FloatField()
    length = models.IntegerField()
    replacement_cost = models.FloatField()
    rating = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    special_features = models.CharField(max_length=255)
    fulltext = models.CharField(max_length=255)
    def __str__(self):
        return self.title

class FilmCategory(models.Model):
    """ 
    Describe the model of FilmCategory use for the Data Base
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "FilmCategories"

class Store(models.Model):
    """ 
    Describe the model of Store use for the Data Base
    """
    manager_staff = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.CharField(max_length=255)
    def __str__(self):
        return "Branch: "+ str(self.address)

class Customer(models.Model):
    """ 
    Describe the model of Customer use for the Data Base
    """
    store = models.ForeignKey(Store, on_delete=models.PROTECT, null=True,  related_name='customer_store')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, null=True,  related_name='customer_address')
    activebool = models.BooleanField()
    create_date = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    active = models.IntegerField()
    def __str__(self):
        return self.first_name

class Staff(models.Model):
    """ 
    Describe the model of Staff use for the Data Base
    """
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, related_name='staff_address', on_delete=models.CASCADE)
    email = models.CharField(max_length=255)
    store = models.ForeignKey(Store, related_name='staff_store', on_delete=models.CASCADE)
    # store = models.IntegerField()
    active = models.BooleanField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    last_update = models.CharField(max_length=255)
    picture = models.CharField(max_length=255, null = True)
    def __str__(self):
        return self.first_name

class Inventory(models.Model):
    """ 
    Describe the model of Inventory use for the Data Base
    """
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    last_update = models.CharField(max_length=255)
    # In Django when you need to modify the plural name in the admin panel
    class Meta:
        verbose_name_plural = "Inventories"

class Rental(models.Model):
    """ 
    Describe the model of Rental use for the Data Base
    """
    rental_date = models.CharField(max_length=255)
    inventory = models.IntegerField()
    customer = models.IntegerField()
    return_date = models.CharField(max_length=255)
    staff = models.IntegerField()
    last_update = models.CharField(max_length=255)
    def __str__(self):
        return str(self.id)


class Payment(models.Model):
    """ 
    Describe the model of Payment use for the Data Base
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.CharField(max_length=255)




