from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    alamat = models.TextField(blank=True, null=True)
    telepon = models.CharField(max_length=20, blank=True, null=True)
    foto = models.ImageField(upload_to='pengguna', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Biodata'
        
    def __Str__(self):
        return self.user.username