from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    def __str__(self):
        return self.name


class Subcategory1(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Automodel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Automodel1(models.Model):
    automodel = models.ForeignKey(Automodel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Automodel2(models.Model):
    automodel1 = models.ForeignKey(Automodel1, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Bestproduct(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    img = models.ImageField(verbose_name='Изображение', upload_to='static/img/bestproduct/')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    price_disc = models.DecimalField(verbose_name='Цена со скидкой', max_digits=7, decimal_places=2, null=True, blank=True)
    new = models.BooleanField(verbose_name='Новый товар')
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Product(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=200)
    description = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    product_code = models.CharField(max_length=32, blank=True, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, blank=True, null=True)
    subcategory1 = models.ForeignKey(Subcategory1, on_delete=models.SET_NULL, blank=True, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    automodel = models.ForeignKey(Automodel, on_delete=models.SET_NULL, blank=True, null=True)
    automodel1 = models.ForeignKey(Automodel1, on_delete=models.SET_NULL, blank=True, null=True)
    automodel2 = models.ForeignKey(Automodel2, on_delete=models.SET_NULL, blank=True, null=True)
    img = models.ImageField(verbose_name='Изображение', upload_to='static/img/bestproduct/', blank=True, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена', default=0)
    price_disc = models.DecimalField(verbose_name='Цена со скидкой', max_digits=7, decimal_places=2, null=True, blank=True)
    new = models.BooleanField(verbose_name='Новый товар', default=False)
    date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)

    def __str__(self):
        return self.name
