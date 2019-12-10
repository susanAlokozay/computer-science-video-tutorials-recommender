from django.db import models

class Category(models.Model):
    catName = models.CharField(max_length=50)
    class Meta:
        db_table = "Category"

class Videos(models.Model):
    vidName = models.CharField(max_length=60)
    vidTopic = models.CharField(max_length=70)
    vidLength = models.CharField(max_length=50)
    vidLecturer = models.CharField(max_length=50)
    vidLanguage = models.CharField(max_length=50)
    vidLocation = models.FileField(max_length=70)
    catId= models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        db_table = "videos"










