from django.urls import path
from . import views

urlpatterns =[
    path('', views.contactformView, name='contact'),
    path('posted/', views.posted),
]