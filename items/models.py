from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255)
    image_b64_addr = models.TextField()
    description = models.TextField()
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    best_before_date = models.DateField(auto_now_add=False, auto_now=False)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
