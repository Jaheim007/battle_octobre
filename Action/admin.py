from django.contrib import admin
from Authentication import models
from Action import models as action

@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display =(
        "username",
    )
    

@admin.register(action.Food_Categories)
class Food_Categories(admin.ModelAdmin):
    list_display =(
        "category_name",
    )
    
@admin.register(action.Food)
class Food(admin.ModelAdmin):
    list_display =(
        "name",
        'image',
        'description',
        'ingredients',
        
    )    