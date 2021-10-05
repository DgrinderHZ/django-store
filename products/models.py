from django.shortcuts import get_object_or_404
from categories.models import Category
from django.db import models
from django.urls import reverse
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products', null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('product_details', args=(self.id,))

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


@receiver(post_save, sender=Product)
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        cat = get_object_or_404(Category, pk=instance.category_id)
        cat.products_count = cat.products_count + 1
        cat.save()
