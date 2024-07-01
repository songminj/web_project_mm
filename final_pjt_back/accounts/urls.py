from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('user_profile/', views.user_profile, name='user_profile'),
]