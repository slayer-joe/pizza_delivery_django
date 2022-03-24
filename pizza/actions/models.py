from django.db import models

class Action(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name="Action name")
    text = models.TextField(verbose_name="Action text")
    imageUrl = models.CharField(max_length=255, verbose_name="image")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Action created")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Actions"
        verbose_name = "Action"
        verbose_name_plural = "Actions"
    