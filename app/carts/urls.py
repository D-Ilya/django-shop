from django.urls import path
from carts import views

app_name = 'carts'

urlpatterns = [
    path('<card_add/',    views.card_add, name='card_add'),
    path('<card_cnange/', views.card_cnange, name='card_cnange'),
    path('<card_remove/', views.card_remove, name='card_remove'),
]
