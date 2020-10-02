from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class TestModel(TestCase):
    def setUp(self):
        self.new_location=Location(name="Kisumu")
        # self.new

    def test_instance(self):
        self.assertTrue(isinstance(self.new_location,Location))

    def test_save(self):
        self.new_location.save_location()
        self.assertTrue(Location.objects.filter(name="Kisumu").exists())

    
    def test_delete(self):
        self.new_location.save_location()
        self.new_location.delete_location()
        self.assertFalse(Location.objects.filter(name="Kisumu").exists())

                                                                                                        