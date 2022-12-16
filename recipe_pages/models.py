from django.db import models

# Create your models here.

# class Measurement(models.Model):
#     measure_amount_description = models.CharField(max_length= 50)

#     def __str__(self):
#         return (self.measure_amount_description)
#     class Meta :
#         db_table = "measurement"
        
# class Ingredient(models.Model):
#     ingredient_name = models.CharField(max_length=30)
#     measurement = models.ForeignKey(Measurement, on_delete=models.DO_NOTHING)
    
#     def __str__(self):
#         return (self.ingredient_name)
#     class Meta :
#         db_table = "ingredient"

# class Image(models.Model):
#     image_path = models.ImageField(upload_to='photos')

#     class Meta :
#         db_table = "image"



class Recipe(models.Model):
    recipe_title = models.CharField(max_length=100)
    preparation = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photos', blank=True, null=True)
    link = models.TextField(blank=True, null=True, max_length=400)

    class Meta :
        db_table = "recipe"

    def __str__ (self) :
        return (self.recipe_title)

# class Recipe_Ingredient(models.Model) :
#     ingredient = models.ForeignKey(Ingredient, on_delete=models.DO_NOTHING)
#     measurement = models.ForeignKey(Measurement, on_delete=models.DO_NOTHING)
#     amount = models.CharField(max_length=50)
    
#     def __str__ (self) :
#         return (self.amount)

#     class Meta :
#         db_table = "recipe_ingredients"
