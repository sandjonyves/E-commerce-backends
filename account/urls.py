from django.urls import path,include
from .views import ClientRegister,ClientLogin

urlpatterns =[
    path('register',ClientRegister.as_view(),name = 'register'),
    path('login',ClientLogin.as_view(),name='login')
]