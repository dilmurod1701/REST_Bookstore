from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username


class BlogPostSubscription(models.Model):
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = 'blogpost'

    def __str__(self):
        return self.email
