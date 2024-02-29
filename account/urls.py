from django.urls import path,include
from .views import *
from rest_framework import routers

route =routers.SimpleRouter()

route.register('client-Register',TestREgister,basename='client')
route.register('marchand-register',MarchantREgister,basename='marchant')
route.register('admin-register',AdminREgister,basename='admin')

urlpatterns =[
    # path('register',ClientRegister.as_view(),name = 'register'),
    
    path('',include(route.urls)),
    path('login',ClientLogin.as_view(),name='login'),
]