from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    path('<int:article_pk>/comments/', views.comments_list, name='comments_list'),
    path('comments/<int:comment_pk>/', views.comment_detail, name='comment_detail'),
]