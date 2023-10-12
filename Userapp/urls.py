from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index),
    path('ViewProduct/<id>', views.Productdetail),
    path('ViewCart', views.ViewCart),
    path('showCart', views.showCart),
    path('removeItem', views.removeItem),
    path('search',views.search),
  
]
