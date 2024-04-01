from django.db import models

from users.models import User
from goods.models import Products


class CartQuertset(models.QuerySet):

    def total_price(self):
        return sum([cart.product_price() * cart.quntity for cart in self])

    def total_quтity(self):
        return sum([cart.quntity for cart in self])


class Cart(models.Model):
    objects = CartQuertset().as_manager()

    user = models.ForeignKey(
        to=User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    session_key = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name='Ключ сессии'
    )
    product = models.ForeignKey(
        to=Products,
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    quntity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name='Количество'
    )
    created_timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления'
    )

    class Meta:
        db_table = 'cart'
        verbose_name = "Корзина"
        verbose_name_plural = 'Корзина'

    def product_price(self):
        return round(self.product.sell_discount(), 2)

    def __str__(self) -> str:
        return f'Корзина "{self.user.username}"|Товар:"{self.product.name}"|Количество:"{self.quntity}"'
