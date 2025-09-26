from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
class BookTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_create_book(self):
        self.client.login(username='testuser', password='password')
        data = {'title': '1984', 'publication_year': 1949, 'authors': 'George Orwell'}
        response = self.client.post('/api/books/create/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        self.client.login(username='testuser', password='password')
        data = {'title': '1984', 'publication_year': 1950}
        response = self.client.put('/api/books/update/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        self.client.login(username='testuser', password='password')
        data = {'title': '1984', 'publication_year': 1950}
        response = self.client.delete('/api/books/delete/1', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
