from django.db import models
# Create your models here.

class about_info(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="")
    des = models.CharField(max_length=1000)

    def __str__(self):
        return self.title