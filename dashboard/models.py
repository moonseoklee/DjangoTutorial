from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    title       = models.CharField(max_length = 20)
    contents    = models.CharField(max_length = 20)
    author = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Comment(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
    comment =  models.CharField(max_length=200)
    author = models.CharField(max_length=20)

    def __str__(self):
        return self.item