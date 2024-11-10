from django.db import models
# Create your models here.
class Plant (models.Model):
    class Category(models.TextChoices):
       FLOWERS = 'Flowers', 'Flowers'
       TREES = 'Trees', 'Trees'
       FRUITS = 'Fruits', 'Fruits'
       VEGETABLES = 'Vegetables', 'Vegetables'

    name = models.CharField(max_length=255)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/" ,default="images/default.png")
    category = models.CharField(max_length=64, choices=Category.choices, default=Category.TREES)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.name