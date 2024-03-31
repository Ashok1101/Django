from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

class Image(models.Model): 
    image_id = models.AutoField
    photo = models.ImageField(upload_to='myimage/',default="")
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.image_id