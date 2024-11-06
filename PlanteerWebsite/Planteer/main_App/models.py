from django.db import models

# Create your models here.
class Contact(models.Model): 
    
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email  = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name