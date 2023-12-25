from django.urls import path
from . import views

urlpatterns =[
    path('', views.parallax_view, name='home'),
]