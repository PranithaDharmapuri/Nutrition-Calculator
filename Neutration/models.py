from django.db import models

class FoodItem(models.Model):
    Name=models.TextField()
    calaries=models.IntegerField()
    protien=models.IntegerField()
    fat=models.IntegerField()
    carbohydrates=models.IntegerField()

    def __str__(self):
        return self.Name
        
