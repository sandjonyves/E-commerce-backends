from django.urls import path,include
from .views import *
from rest_framework import routers

route =routers.SimpleRouter()

route.register('user',UserRegister,basename='user')

route.register('client',ClientUser,basename='client')
route.register('marhand',MarchandUser,basename='marchand')
route.register('admin',AdminUser,basename='admin')
# route.register('marchand-register',MarchantREgister,basename='marchant')
# route.register('admin-register',AdminREgister,basename='admin')

urlpatterns =[
    # path('register',ClientRegister.as_view(),name = 'register'),
    
    path('',include(route.urls)),
    # path('user/client/',ClientUser.as_view(),name='user'),
    
    # path('client',ClientUser.as_view(),name='client'  ),
    path('login',UserLogin.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
]