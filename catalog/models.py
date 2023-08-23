from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    photo = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение/превью')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=100, verbose_name='Категория')
    price_for_purchase = models.IntegerField(verbose_name='Цена за покупку')
    creation_date = models.DateField(verbose_name='Дата изготовления')
    last_change_date = models.DateField(verbose_name='Дата изменения', auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.price_for_purchase}, {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
