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
admin.site.register(CreateBkash)
admin.site.register(WhishLIst)

admin.site.site_header = 'My Site Admin Panel'
admin.site.site_title = 'My Site Title'