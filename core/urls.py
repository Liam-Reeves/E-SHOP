from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    path('', views.index, name="index"),
    
    path('products/', views.products, name="products"),
    
    path('about/', views.about, name="about"),
    
    path('contact/', views.contact, name="contact"),
    
    path('cart/', views.cart, name="cart"),
    
    path('', views.checkout, name="checkout"),
    
    path('subscribe/', views.subscribe, name="subscribe"),
    
    

      
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
