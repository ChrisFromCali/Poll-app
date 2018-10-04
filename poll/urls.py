from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='poll-home'),
    path('create/', views.create, name='poll-create'),
    path('view/<int:poll_id>', views.view, name='poll-view'),
]