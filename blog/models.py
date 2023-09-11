from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Materials(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='изображение/превью', **NULLABLE)
    created_at = models.DateField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмоторы')

    def __str__(self):
        return f'{self.title}, {self.content}'

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
