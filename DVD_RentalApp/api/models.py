from django.db import models
  
# class Item(models.Model):
#     category = models.CharField(max_length=255)
#     subcatgeory = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     amount = models.PositiveIntegerField()
  
#     def __str__(self) -> str:
#         return self.name

# from movies.models import Movie

# class MovieResource(ModelResource):
#     class Meta:
#         queryset = Movie.objects.all()
#         resource_name = 'movies'

# Create / Insert / Add POST
# Retrive / Fetch GET
# Update / Edit PUT
# Deletes / Remove DELETE

# class Film(models.Model):
#     [film_id] INT,
# [title] VARCHAR,
# [description] VARCHAR,
# [release_year] INT,
# [language_id] INT,
# [rental_duration] INT,
# [rental_rate] FLOAT,
# [length] INT,
# [replacement_cost] FLOAT,
# [rating] VARCHAR,
# [last_update] VARCHAR,
# [special_features] VARCHAR,
# [fulltext] VARCHAR
