from django.urls import include, path
from . import views

urlpatterns =[
   #path('', views.index),
   path('', views.listing),
   path('<int:album_id>/', views.detail),
   path('search/', views.search),
]