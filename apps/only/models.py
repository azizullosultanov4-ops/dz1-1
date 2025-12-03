from django.db import models 

# Create your models here.
class Settings(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок сайта ")
    descriptions = models.TextField(verbose_name="Описание сайта")
    phone = models.CharField(max_length=100, verbose_name="Номер телефона ")
    email = models.EmailField(verbose_name="Электронная почта")
    address = models.CharField(max_length=100, verbose_name="Адрес сайта ")
    logo = models.ImageField(upload_to='logos/',verbose_name="Логотип сайта ") 

    class Meta:
        verbose_name = "Название сайт"
        verbose_name_plural = "Названии сайта" 

    def __str__(self):
        return self.title


# Create your models here.
