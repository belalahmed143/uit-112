from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Banner)
admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImageGallery

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

admin.site.register(Product,ProductAdmin)
admin.site.register(CartProduct)
admin.site.register(Order)