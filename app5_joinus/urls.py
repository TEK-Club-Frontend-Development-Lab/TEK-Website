from django.urls import path
from . import views

app_name = 'joinus'

urlpatterns = [
    path('apply/', views.apply, name='apply'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq')
]