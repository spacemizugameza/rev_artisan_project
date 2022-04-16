from django.urls import path
from .import views


urlpatterns = [
    path('',views.home_p,name='home-page'),
    path('about/',views.about_p,name='about-page'),
    path('contact/',views.contact_p,name='contact-page'),
    # path('product/',views.product_p,name='product-page'),
    
]
