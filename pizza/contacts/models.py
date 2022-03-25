from django.db import models

class Contact(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Shop title")
    adress = models.TextField(verbose_name="Shop adress")
    phone = models.TextField(verbose_name="Shop phone number")
    shop_image_src = models.CharField(max_length=255, verbose_name="image")

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "Shops"
        verbose_name = "Shop"
        verbose_name_plural = "Shops"