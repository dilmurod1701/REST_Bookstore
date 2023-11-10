from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    category_choice = (
        ('qorqinchli', 'qorqinchli'),
        ('tarixiy', 'tarixiy'),
        ('adabiy', 'adabiy'),
        ('sher', 'sher'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=90)
    about_book = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category_choice)
    is_available = models.BooleanField()
    published = models.DateField()
    ISO = models.BigIntegerField()

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title
