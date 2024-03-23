from django.urls import path,include
from .views import *
from rest_framework import routers

route =routers.SimpleRouter()

route.register('register',UserRegister,basename='client')

# route.register('read/<use_type>',ReadOnlyUser,basename='read')
# route.register('marchand-register',MarchantREgister,basename='marchant')
# route.register('admin-register',AdminREgister,basename='admin')

urlpatterns =[
    # path('register',ClientRegister.as_view(),name = 'register'),
    
    path('',include(route.urls)),
    # path('user',UserRegister.as_view(),name='user'),
    path('read',ReadOnlyUser.as_view(),name='read'  ),
    path('login',UserLogin.as_view(),name='login'),
    path('logout',Logout.as_view(),name='login'),
]