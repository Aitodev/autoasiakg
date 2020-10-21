from django.db import models

class Bestproduct(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    img = models.ImageField(verbose_name='Изображение', upload_to='static/img/bestproduct/')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    price_disc = models.DecimalField(verbose_name='Цена со скидкой', max_digits=7, decimal_places=2, null=True,
                                     blank=True)
    new = models.BooleanField(verbose_name='Новый товар')
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'