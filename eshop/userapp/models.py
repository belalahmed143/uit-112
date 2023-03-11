from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length = 150,blank=True, null=True)
    image  = models.ImageField(upload_to='ProfileImage', default='ProfileImage/no_profile.png')
    
    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.user.username

