from django.urls import path
from . import views

app_name = 'finances'

urlpatterns = [
    path('save_exchange_rate/', views.save_exchange_rate, name='save_exchange_rate'),
    path('exchange_rate/', views.exchange_rate, name='exchange_rate'),
    path('save_address/', views.save_address, name='save_address'),
    path('address/', views.address, name='address'),
    path('save_bank/', views.save_bank, name='save_bank'),
    path('bank/', views.bank, name='bank'),
]