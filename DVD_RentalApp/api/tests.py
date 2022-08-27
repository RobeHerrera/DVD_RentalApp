from django.test import TestCase
from movies.models import Movie, Genre

# TODO
# 1. Add test for Authentication 
# 2. Add for all end points in the API

"""
Added some simple Test Cases for demostration of the unit test

run inside of the venv: 
    python manage.py test
    
"""

class HomepageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class MovieTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.genre = Genre.objects.create(name="mygenre")
        cls.movie = Movie.objects.create(
            title="Title",
            release_year=1990,
            number_in_stocks=1,
            daily_rate=1.1,
            genre=cls.genre,
            date_created="2022-10-10"
        )

    def test_model_content(self):
        self.assertEqual(self.movie.title, "Title")
        self.assertEqual(self.movie.release_year, 1990)
        self.assertEqual(self.movie.number_in_stocks, 1)
        self.assertEqual(self.movie.daily_rate, 1.1)
        self.assertEqual(self.movie.genre, self.genre)
        self.assertEqual(self.movie.date_created, "2022-10-10")

    def test_list_url(self):
        response = self.client.get("/api/movies/list/")
        self.assertEqual(response.status_code, 200)


