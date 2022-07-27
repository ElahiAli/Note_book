from django.db import models
from django.conf import settings


# Create your models here.
class Notes(models.Model):
    name = models.CharField(max_length=255)
    discriptions = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)