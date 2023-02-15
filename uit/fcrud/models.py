from django.db import models

# Create your models here.
class StudentData(models.Model):
    name = models.CharField(max_length = 150)
    roll = models.CharField(max_length = 150, unique=True)
    s_class = models.CharField(max_length = 150)

    def __str__(self):
        return self.name
    
    
    
