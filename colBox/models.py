
from unicodedata import name
from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)
    
    @classmethod
    def get_all(cls):
        '''
        method to retrive all stored locations
        '''
        loc = Location.objects.all()
        return loc
    
    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()
        
    def delete_location(self):
            self.delete()
    
    @classmethod
    def update_location(cls, search_term , new_locale):
        '''
        method to update a location's city name
        '''
        try:
            to_update = Location.objects.get(name = search_term)
            to_update.name = new_locale
            to_update.save()
            return to_update
        except Location.DoesNotExist:
            print('Location you specified does not exist')
  
    
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
    
    def save_category(self):
            self.save()
    
    def delete_category(self):
            self.delete()
    
    @classmethod
    def update_category(cls, search_term , new_cat):
        '''
        method to update a category
        '''
        try:
            to_update = Category.objects.get(name = search_term)
            to_update.name = new_cat
            to_update.save()
            return to_update
        except Category.DoesNotExist:
            print('Category you specified does not exist')

    
    
    
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
    
    def update_image(self, new_image):
        try:
            self.image = new_image
            self.save()
            return self
        except self.DoesNotExist:
            print('Images already exists')
    
    @classmethod
    def get_image_by_id(cls, id):
        '''
        method to retrieve images by unique id
        '''
        retrieved = Image.objects.get(id = id)
        return retrieved
    
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
    
    @classmethod
    def search_images(cls, search_term):
        images = cls.objects.filter(imageCategory__name__icontains=search_term)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = cls.objects.filter(imageLocation__name__icontains=location).all()
        return images