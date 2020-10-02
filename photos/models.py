from django.db import models
from django.utils.text import slugify

# Create your models here.
class Image(models.Model):
    name=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200)
    image=models.ImageField(upload_to='photos/%Y/%m/%d/')
    description=models.TextField(blank=True)
    location=models.ForeignKey("Location",on_delete=models.CASCADE)
    category=models.ManyToManyField("Category")
    

    
    @classmethod
    def search_image(cls,user_input):
        images=cls.objects.filter(category__name__icontains=user_input)
        return images
    
    def __str__(self):
        return self.name
    
        
  
class Location(models.Model):
    name=models.CharField(max_length=50)
     
    def __str__(self):
        return self.name

    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name_plural="Category"

    



