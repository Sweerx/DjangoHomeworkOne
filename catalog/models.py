from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, help_text='Введите описание')
    images = models.ImageField(upload_to='catalog/photo', verbose_name='Фото', blank=True, null=True,
                               help_text='Загрузите фото')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, max_length=100, verbose_name='Категория',
                                 help_text='Введите категорию')
    purchase_price = models.IntegerField(verbose_name='Цена покупки', help_text='Введите цену покупки')
    created_at = models.DateField(verbose_name='Дата создания', help_text='Введите дату создания')
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', blank=True, null=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'created_at']

    def __str__(self):
        return self.name, self.description


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
