from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking', views.booking, name='booking'),
    path('about/', views.about, name='about'),
    path('amzingwild/', views.amazing, name='amazingwild'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('blog/', views.hotels, name='blog'),
    path('blog/<str:id>/', views.blogdetail, name='blogdetail'),
    path('safarissymphony/', views.safaris, name='safaris'),
    path('safaris/', views.tours, name='tours'),
    path('ultimateeastafrica/', views.ultimateeastafrica, name='ultimateeastafrica'),
    path('visitkenya/', views.visitkenya, name='visitkenya'),
    path('coastalcharms/', views.visittz, name='visittz'),
    path('heartofthepearl', views.visituganda, name='visituganda'),
    path('whispersofthewild', views.visitrwanda, name='visitrwanda'),
    path('privacy+policy', views.privacy, name='privacy')
]