from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

difficulties=[('Hard','Hard'),('Medium','Medium'),('Easy','Easy')]
class Tags(models.Model):
    Name=models.CharField(max_length=50,primary_key=True)

class Questions(models.Model):
    Title=models.CharField(max_length=70,blank=False)
    Difficulty=models.CharField(max_length=50,choices=difficulties)
    Acceptance=models.IntegerField(default=0,validators=[MaxValueValidator(100),MinValueValidator(0)])
    Submissions=models.IntegerField(default=0)
    Accepted=models.IntegerField(default=0)
    Likes=models.IntegerField(default=0)
    DisLikes=models.IntegerField(default=0)
    Tags=models.ManyToManyField(Tags)
    Text=models.TextField()

