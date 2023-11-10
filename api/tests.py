from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from selenium import webdriver

from .models import Book

# Create your tests here.


class TestModels(TestCase):
    def setUp(self) -> None:
        Book.objects.create(user=User.objects.create_user(username='alabay', password='alabay01'), title='serikboy', about_book='kfdjgbn', category='qorqinchli', is_available='True', published='2023-11-25', ISO='232378263')
        Book.objects.create(user=User.objects.create_user(username='speed', password='speed01'), title='speed', about_book='aspfgnf', category='tarixiy', is_available='True', published='2023-11-13', ISO='27376324')
        Book.objects.create(user=User.objects.create_user(username='chingiz', password='chingiz01'), title='chingiz', about_book='skweu3', category='qorqinchli', is_available='False', published='2021-11-25', ISO='93462')
        Book.objects.create(user=User.objects.create_user(username='olik', password='olik01'), title='olik', about_book='sher', category='sher', is_available='True', published='2023-11-25', ISO='9386223')

    def test_title(self):
        obj1 = Book.objects.get(title='serikboy')
        obj2 = Book.objects.get(title='speed')
        obj3 = Book.objects.get(title='chingiz')
        obj4 = Book.objects.get(title='olik')
        self.assertEquals(obj1.title, 'serikboy')
        self.assertEquals(obj2.title, 'speed')
        self.assertEquals(obj3.title, 'chingiz')
        self.assertEquals(obj4.title, 'olik')

    def test_ISO(self):
        obj1 = Book.objects.get(ISO='232378263')
        obj2 = Book.objects.get(ISO='27376324')
        obj3 = Book.objects.get(ISO='93462')
        obj4 = Book.objects.get(ISO='9386223')
        self.assertEquals(obj1.ISO, 232378263)
        self.assertEquals(obj2.ISO, 27376324)
        self.assertEquals(obj3.ISO, 93462)
        self.assertEquals(obj4.ISO, 9386223)


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        Book.objects.create(user=User.objects.create_user(username='alabay', password='alabay01'), title='serikboy', about_book='kfdjgbn', category='qorqinchli', is_available='True', published='2023-11-25', ISO='232378263')
        Book.objects.create(user=User.objects.create_user(username='speed2', password='speed01'), title='speed', about_book='aspfgnf', category='tarixiy', is_available='True', published='2023-11-13', ISO='27376324')
        Book.objects.create(user=User.objects.create_user(username='chingiz2', password='chingiz01'), title='chingiz', about_book='skweu3', category='qorqinchli', is_available='False', published='2021-11-25', ISO='93462')
        Book.objects.create(user=User.objects.create_user(username='olik2', password='olik01'), title='olik', about_book='sher', category='sher', is_available='True', published='2023-11-25', ISO='9386223')

    def test_web_site(self):
        response = self.client.get('http://127.0.0.1:8000/api/all')
        return self.assertEquals(response.json()[0]['title'], 'serikboy')


class BookSelenium(TestCase):
    def setUp(self) -> None:
        Book.objects.create(user=User.objects.create_user(username='alabay', password='alabay01'), title='serikboy', about_book='kfdjgbn', category='qorqinchli', is_available='True', published='2023-11-25', ISO='232378263')
        Book.objects.create(user=User.objects.create_user(username='speed2', password='speed01'), title='speed', about_book='aspfgnf', category='tarixiy', is_available='True', published='2023-11-13', ISO='27376324')
        Book.objects.create(user=User.objects.create_user(username='chingiz2', password='chingiz01'), title='chingiz', about_book='skweu3', category='qorqinchli', is_available='False', published='2021-11-25', ISO='93462')
        Book.objects.create(user=User.objects.create_user(username='olik2', password='olik01'), title='olik', about_book='sher', category='sher', is_available='True', published='2023-11-25', ISO='9386223')

    def test_site(self):
        self.client = APIClient()
        response = webdriver.Chrome()
        response.get('http://127.0.0.1:8000/api/all')
        assert 'ISO' in response.page_source
