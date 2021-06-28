from django.test import TestCase, Client
from film.models import Movie, Actor


class TestSongViewSet(TestCase):
    def setUp(self) -> None:
        self.movie = Movie.objects.create(name='Test movie', year='2000', imdb=7.2, genre='Comedy')
        self.client = Client()

    def test_filter_imdb_movies(self):
        response = self.client.get('/movies/?ordering=-imdb')
        data = response.data
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)




    def test_search_movies(self):
        response = self.client.get('/movies/?search=Test movie')
        data = response.data
        print(data)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], "Test movie")
        self.assertEquals(data[0]['year'], "2000")
        self.assertEquals(data[0]['imdb'], 7.2)
        self.assertEquals(data[0]['genre'], "Comedy")

    def test_get_movies(self):
        response = self.client.get('/movies/')
        self.assertEquals(response.status_code, 200)