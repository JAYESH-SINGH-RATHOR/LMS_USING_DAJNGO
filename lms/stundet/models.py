from django.db import models
# Create your models here.

class about_info(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="")
    des = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
class contact_info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200 ,  blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class RegisteredUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    course = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name