from django.urls import path,include
from .views import ClientRegister,ClientLogin,TestREgister
from rest_framework import routers

route =routers.SimpleRouter()

route.register('testRegister',TestREgister,basename='test')

urlpatterns =[
    path('register',ClientRegister.as_view(),name = 'register'),
    path('login',ClientLogin.as_view(),name='login'),
    # path('',include(route.urls)),
]