
from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    categories = (
        ('Selfies','Selfies'),
        ('Food','Food'),
        ('Cars','Cars'),
        ('Swimming','Swimming'),
        ('Football','Football'),
        ('Parks','Parks'),
        ('Forest','Forest'),
    )
    name = models.CharField(max_length=40, choices = categories)
    
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/',default='')
    imageName= models.CharField(max_length=70)
    imageDescription= models.TextField()
    imageLocation= models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    imageCategory= models.ForeignKey(Category, on_delete=models.CASCADE, default='')
    pub_date= models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.imageName
    
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def get_images(cls):
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
 
