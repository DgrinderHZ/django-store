from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class UserProfile(models.Model):
    address = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
