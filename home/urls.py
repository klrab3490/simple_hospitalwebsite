from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='home' ),
    path('about', views.about ,name='about'),
    path('contact', views.contact,name='contact' ),
    path('doctors', views.doctors,name='doctors' ),
    path('booking', views.booking , name='booking'),
    path('departments', views.department, name='department' ),
]