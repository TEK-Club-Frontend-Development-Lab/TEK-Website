from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('announcement/', views.announcement, name='announcement'),
    path('event/', views.event, name='event'),
]