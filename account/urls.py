from django.urls import path,include
from .views import *
from rest_framework import routers

route =routers.SimpleRouter()

route.register('client-Register',ClientRegister,basename='client')
route.register('marchand-register',MarchantREgister,basename='marchant')
route.register('admin-register',AdminREgister,basename='admin')

urlpatterns =[
    # path('register',ClientRegister.as_view(),name = 'register'),
    
    path('',include(route.urls)),
    path('login',UserLogin.as_view(),name='login'),
]