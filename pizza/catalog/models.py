from django.db import models
from datetime import datetime
from random import randint

class PizzaModel(models.Model):

    def file_path(self, filename):
        file_type = filename.split('.')[-1]
        path_file = datetime.strftime(datetime.now(), "post/%Y/%m/%d")
        return path_file + str(randint(1000000, 9999999)) + "." + file_type

    title = models.CharField(max_length=50, unique=True, verbose_name="Pizza name")
    cathegory = models.ManyToManyField("Category", related_name="pizza")
    text = models.TextField(verbose_name="Post data")
    price = models.IntegerField(default=15)
    image = models.CharField(max_length=255, verbose_name="image")

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "Pizza"
        verbose_name = "Pizza"
        verbose_name_plural = "Pizza"


class Category(models.Model):
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.value
    
    class Meta:
        db_table = "Category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
