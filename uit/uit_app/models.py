from django.db import models
# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Product(models.Model):
    image = models.ImageField(upload_to='Product')
    title = models.CharField(max_length = 150)
    description = models.TextField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length = 150)
    phone = models.CharField(max_length = 150)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name + ' / ' + self.phone