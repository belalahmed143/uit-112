from django.db import models

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
    
    
    
    
    