from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save #события модели например что делать перед сохранениемб или перед удалением и т.д.
from django.dispatch.dispatcher import receiver

class User(AbstractUser): #модель это таблица в БД
    phone = models.CharField(max_length=15, verbose_name="User phone")

    class Meta:
        db_table = "users" #создается таблица с именем users, а не сгенерируемы именем
        verbose_name = 'User'
        verbose_name_plural = "User Models"
        # unique_together = ("username", "password")

    def __str__(self) -> str:
        return self.username

@receiver(pre_save, sender=User) # декоратор событий модели, создает обработчик события
def hash_password(sender, instance, **kwargs): 
    # sender - модель у которой смотрим событие
    # instance - обьект созданный на основе этой модели(в частности User) 
        if (instance.id is None) or (
            sender.objects.get(id=instance.id).password != instance.password
            ): # это запрос в базу
               # ищем обьект под id = instance.id и сравниваем его пароль с текущим
                instance.set_password(instance.password) #этот метод хеширует пароль
