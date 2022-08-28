from django.contrib import admin
from .models import (
    Genre, Movie, Actor, Address, Category, City, Country, Customer,
    FilmCategory, Film, Inventory, Language, Payment, Rental, Staff, Store
    )


"""
To show in admin page

TODO: 
    - Add all the tables in the DB of DVD Rental
"""
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )
    list_display = ('id', 'title', 'number_in_stocks', 'daily_rate', 'genre')

class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'last_update')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'address2', 'district'
    ,'city','postal_code','phone','last_update')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_update')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'country', 'last_update')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'last_update')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    exclude = ('active',)
    list_display = ('id', 'store', 'first_name','last_name', 
    'email','address','activebool','create_date','last_update')

@admin.register(FilmCategory)
class FilmCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'last_update')

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description','release_year','language',
    'rental_duration','rental_rate','length','replacement_cost','rating',
    'last_update','special_features','fulltext')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'store','last_update')

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_update')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'staff','rental','amount',
    'payment_date')

@admin.register(Rental)
class RentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'rental_date', 'inventory','customer','return_date',
    'staff', 'last_update')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    exclude = ('picture', )
    list_display = ('id', 'first_name', 'last_name','address','email',
    'store','active','username','password','last_update')

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    exclude = ('picture', )
    list_display = ('id', 'manager_staff', 'address', 'last_update')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Address, AddressAdmin)
