from django.urls import path
from . import views

app_name ='mobil'

urlpatterns = [
    path('tambah/', views.TambahMobil.as_view(), name='tambah'),
    path('', views.IndexMobil.as_view(), name='index'),
]