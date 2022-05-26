
from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)
    
    
class Category(models.Model):
    name = models.CharField(max_length=40)
   
class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='')
    imageName= models.CharField(max_length=70)
    imageDescription= models.TextField()
    imageLocation= models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    # imageCategory= models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    pub_date= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.imageName
    
    def save_image(self):
        self.save()
        
    @classmethod
    def get_images(cls):
        # today = dt.date.today()
        images = cls.objects.all()
        return images
    
    @classmethod
    def today_images(cls):
        today = dt.date.today()
        images = cls.objects.filter(pub_date__date=today)
        return images
        
    @classmethod
    def get_latest(cls):
        images = cls.objects.last()
        return images
 
