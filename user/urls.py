from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_search, name='user-search'),
    path('<str:username>/', views.user, name='user')
]