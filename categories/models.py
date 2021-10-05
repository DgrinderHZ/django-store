from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    products_count = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
