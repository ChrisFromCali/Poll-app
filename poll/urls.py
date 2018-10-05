from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='poll-home'),
    path('create/', views.create, name='poll-create'),
    path('view/<int:poll_id>', views.view, name='poll-view'),
    path('vote/<int:poll_id>', views.vote, name='poll-vote'),
    path('results/<int:poll_id>', views.results, name='poll-results')
]