from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'  # То, что в БД
        verbose_name = "Категория"  # В админ панельке
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True,
                            verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True,
                            blank=True, null=True, verbose_name='URL')
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images',
                              blank=True, null=True, verbose_name='Изображнеие')
    price = models.DecimalField(
        default='0.00', max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(
        default='0.00', max_digits=4, decimal_places=2, verbose_name='Скидка%')
    quantity = models.PositiveIntegerField(
        default=0, verbose_name='Количество')
    category_id = models.ForeignKey(to=Categories, on_delete=models.PROTECT)

    class Meta:
        db_table = 'product'
        verbose_name = "Продукт"
        verbose_name_plural = 'Продукты'
        ordering = ("id",)

    def __str__(self) -> str:
        return f'{self.name} Количество - {self.quantity}'

    def display_id(self):
        return f'{self.id:05}'

    def sell_discount(self):
        if self.discount:
            res = round(self.price - (self.price * self.discount / 100), 2)
            return f'{res}'
        return f'{self.price}'
