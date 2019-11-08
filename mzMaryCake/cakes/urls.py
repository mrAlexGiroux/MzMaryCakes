from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:cake_ID>/', views.cakeDetails, name='cake'),
    path('', views.aboutMe, name='aboutMe'),
]