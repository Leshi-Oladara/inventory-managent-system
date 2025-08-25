from django.db import models

# Create your models here.

CATEGORY=(
    ("drugs", "drugs"),
    ("fruits", "fruits"),
    ("food","food"),
)

class product(models.Model):
    name = models.CharField(max_length=100, blank=True)
    category= models.CharField(max_length=100, choices=CATEGORY,blank=True)
    quantity= models.PositiveIntegerField(null=True)