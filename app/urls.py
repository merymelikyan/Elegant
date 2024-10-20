from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('premium/', views.premium, name="premium"),
    path('products/', views.products, name="products"),
    
] 