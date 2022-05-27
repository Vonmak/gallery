from unicodedata import name
from django.test import TestCase
from .models import Image, Category, Location

# Create your tests here.
class ImagesTest(TestCase):
    '''
    test class for Images model
    '''
    def setUp(self):
        '''
        test method to create Image instances called before all tests
        '''
        self.new_category = Category(name='testing')
        self.new_category.save_category()
        
        self.new_location = Location(name='Nairobi')
        self.new_location.save_location()
        
        self.new_picture = Image(image='images/picture.jpeg', imageName='Image title', imageDescription='sth random', imageCategory=self.new_category, imageLocation=self.new_location)
        self.new_picture.save_image()
        self.another_picture = Image(image='images/photo.jpg', imageName='Another title', imageDescription='sth else more random', imageCategory=self.new_category, imageLocation=self.new_location)
        self.another_picture.save_image()

    def tearDown(self):
        '''
        test method to delete Image instances after each test is run
        '''
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.assertTrue(len(Image.objects.all()) == 2)
        
    def test_instances(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.new_picture,Image))
        self.assertTrue(isinstance(self.new_category, Category))
        self.assertTrue(isinstance(self.new_location, Location))


    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.new_picture.delete_image()
        self.assertTrue(len(Image.objects.all()) == 1)

    def test_update_image(self):
        '''
        test method to ensure an Image instance has been correctly updated
        '''
        update_test = self.new_picture.update_image('images/updated.png')
        self.assertEqual(update_test.image, 'images/updated.png')

    def test_get_images(self):
        '''
        test method to ensure all instances of Image class have been retrieved
        '''
        pictures = Image.get_images()
        print(pictures)

    def test_get_image_by_id(self):
        '''
        test method to ensure Image instances can be retrieved by id
        '''
        obtained_image = Image.get_image_by_id(self.another_picture.id)
        print(obtained_image.imageName)

    def test_search_image(self):
        '''
        test method to ensure correct searching of an multiple image instances by category
        '''
        obtained_image = Image.search_images(self.new_picture.imageCategory)
        print(obtained_image) #todo: reference individual instances

    def test_filter_by_location(self):
        '''
        test method to obtain image instances by location
        '''
        obtained_image = Image.filter_by_location(self.another_picture.imageLocation)
        print(obtained_image)



class CategoryTest(TestCase):
    '''
    test class for Category model
    '''
    def setUp(self):
        '''
        test method to create Category instances called before all tests
        '''
        self.new_category = Category(name='categoryA')
        self.new_category.save_category()

    def tearDown(self):
        '''
        test method to delete Category instances after each test is run
        '''
        Category.objects.all().delete()

    def test_save_category(self):
        '''
        test method to ensure a Category instance has been correctly saved
        '''
        self.assertTrue(len(Category.objects.all()) == 1)     

    def test_delete_category(self):
        '''
        test method to ensure a Category instance has been correctly deleted
        '''
        self.new_category.save_category()
        self.new_category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)    

    def test_update_category(self):
        '''
        test method to ensure a Category instance has been correctly updated
        '''
        update_cat = Category.update_category('categoryA', 'differentCat')
        self.assertEqual(update_cat.name, 'differentCat')




class LocationTest(TestCase):
    '''
    test class for Location model
    '''
    def setUp(self):
        '''
        test method to create Location instances called before all tests
        '''
        self.new_location = Location(name='lost city')
        self.new_location.save_location()

    def test_save_location(self):
        '''
        test method to ensure a Location instance has been correctly saved
        '''
        self.assertTrue(len(Location.objects.all()) == 1)     

    def test_delete_location(self):
        '''
        test method to ensure a Location instance has been correctly deleted
        '''
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

    def test_update_location(self):
        '''
        test method to ensure a Location instance has been correctly updated
        '''
        update_locale = Location.update_location('lost city', 'paperTown')
        self.assertEqual(update_locale.name,'paperTown')

    def test_get_all(self):
        '''
        test method to ensure all instances of Location class have been retrieved
        '''
        locations = Location.get_all()
        print(locations)