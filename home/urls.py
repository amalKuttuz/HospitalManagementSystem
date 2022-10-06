from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    
    path('depp',views.depp,name="depp"),
    
    path('contact',views.contact,name="contact"),
    
    path('doctors',views.doc,name="doctors"),
    
    path('booking',views.booking,name="booking"),
]