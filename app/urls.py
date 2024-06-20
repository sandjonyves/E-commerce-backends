from django.urls import path,include
from .views import *
from rest_framework import routers
route = routers.SimpleRouter()

route.register('marque',MarqueViewSet,basename='marque')
# route.register('modele',ModeleViewSet,basename='modele')
# route.register('voiture',VoitureViewSet ,basename='voiture')

urlpatterns =[
    path('',include(route.urls)),
    # path('search-marqueModele/<id>/', SearchModeleMarque.as_view(), name='read_marque'),

]