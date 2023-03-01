from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='Banner')
    http_link = models.URLField(max_length = 200)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name  = models.CharField(max_length = 150)
    parent_category  = models.ForeignKey('self', related_name='chaild',  on_delete=models.CASCADE, blank=True, null=True)
    icon = models.CharField(max_length = 150)
    image  = models.ImageField(upload_to='Category')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 250)
    code  = models.CharField(max_length = 150)
    category  = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productImage',blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    price  = models.IntegerField()
    discount_price  = models.IntegerField(blank=True, null=True)
    purchase_price = models.IntegerField()
    purchase_quantity = models.IntegerField()
    available_stock  = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


class ProductImageGallery(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    another_image = models.ImageField(upload_to='productImageGallery')
    
    class Meta:
        verbose_name_plural = 'ProductImageGallerys'

    def __str__(self):
        return self.product.name
    
    
    
    
    