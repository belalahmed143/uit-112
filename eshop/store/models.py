from django.db import models

# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='Banner')
    http_link = models.URLField(max_length = 200)

    def __str__(self):
        return self.title
    
    
    