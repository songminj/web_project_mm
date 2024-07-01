from django.urls import path
from . import views

app_name = 'deposits'

urlpatterns = [
    path('', views.example, name='example'),
    path('save_deposit_prdts/', views.save_deposit_prdts, name='save_deposit_prdts'),
    path('deposit_prdts/', views.deposit_prdts, name='deposit_prdts'),
    path('update_deposit_cart/<int:product_pk>/', views.update_deposit_cart, name='update_deposit_cart'),
    path('deposit_cart/', views.deposit_cart, name='deposit_cart'),
    path('deposit_cart_option/', views.deposit_cart_option, name='deposit_cart_option'),
    path('save_deposit_options/', views.save_deposit_options, name='save_deposit_options'),
    path('deposit_options/', views.deposit_options, name='deposit_options'),
]