from django.urls import path,include
from .views import *
urlpatterns =[
    path('login/',login,name="login"),
    path('auth/', include('social_django.urls', namespace='social')),
     path('home/', home, name='home'),
     path('logout/',logoutt,name="logout"),
     path('profile/',profile,name="profile"),
     

   
]