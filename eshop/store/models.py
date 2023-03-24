from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from django.contrib.auth.models import User

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='Banner')
    http_link = models.URLField(max_length = 200)

    def __str__(self):
        return "Test /" + str(self.id)
    
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

class CartProduct(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity  = models.IntegerField(default=1)
    ordered  = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'CartProducts'

    def __str__(self):
        return self.product.name

    def get_subtotal(self):
        if self.product.discount_price:
            return self.product.discount_price * self.quantity
        else:
            return self.product.price * self.quantity

class Checkout(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    full_address  = models.CharField(max_length = 250)
    phone  = models.CharField(max_length = 150)
    email  = models.EmailField()
    order_note  = models.TextField()
    
    def __str__(self):
        return self.user.username


class Order(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    products  = models.ManyToManyField(CartProduct)
    ordered  = models.BooleanField(default=False)
    ordered_date  = models.DateTimeField(blank=True, null=True)
    payment_option  = models.CharField(max_length = 150,blank=True, null=True)
    shipping_address = models.ForeignKey(Checkout, on_delete=models.CASCADE,blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for i in self.products.all():
            total += i.get_subtotal()
        return total
    
class CreateBkash(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentID  = models.CharField(max_length = 150)
    
    
    
    
    
    