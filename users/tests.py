from django.test import TestCase
from django.contrib.auth.models import User

from .models import Profile, BlogPostSubscription
# Create your tests here.


class TestModels(TestCase):
    def setUp(self) -> None:
        BlogPostSubscription.objects.create(email='john@gmail.com')
        BlogPostSubscription.objects.create(email='speed@gmail.com')
        BlogPostSubscription.objects.create(email='saparboy@gmail.com')
        BlogPostSubscription.objects.create(email='kasha@gmail.com')

    def test_email(self):
        obj1 = BlogPostSubscription.objects.get(email='john@gmail.com')
        obj2 = BlogPostSubscription.objects.get(email='speed@gmail.com')
        obj3 = BlogPostSubscription.objects.get(email='saparboy@gmail.com')
        obj4 = BlogPostSubscription.objects.get(email='kasha@gmail.com')
        self.assertEquals(obj1.email, 'john@gmail.com')
        self.assertEquals(obj2.email, 'speed@gmail.com')
        self.assertEquals(obj3.email, 'saparboy@gmail.com')
        self.assertEquals(obj4.email, 'kasha@gmail.com')

