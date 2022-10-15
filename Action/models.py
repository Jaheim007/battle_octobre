from django.db import models
from ckeditor.fields import RichTextField

from Authentication.models import RepeatFields

class Food_Categories(RepeatFields):
    category_name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.category_name

class Food(RepeatFields):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="Food_Images")
    category = models.ForeignKey(Food_Categories , on_delete=models.SET_NULL, null=True , related_name='category')
    description = RichTextField(blank=True , null=True)
    ingredients = RichTextField(blank=True , null=True)
    
    
    

