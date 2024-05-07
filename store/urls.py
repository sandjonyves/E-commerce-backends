from django.urls import path,include
from rest_framework import routers
from .views import *

router =  routers.SimpleRouter()
router.register(r'piece',PierceViewSet)
router.register('cathegorie',cathegorieViewSet)
router.register('commande',CommandeViewSet,basename='commande')
router.register('read',Read,basename='read')
urlpatterns=[
    # path('admin/', admin.site.urls),
    # path('auth/',include('rest_framework.urls')),
    # path('store',include('Store.urls'),name='store'),
   
    # path('test2/<int:pk>/',PierceViewSet.as_view({'patch':'update'})),
    path('',include(router.urls)),
    path('read-all-cathegorie-of-model/<id>',SearchModelCathegorie.as_view(),name='seach-cathegorie-of-model')
    

    # path('get_cathegorie/<int:id>',cathegorieViewSet.as_view({'get':'get_cathegorie'})),
    # path('get_piece/<int:id>',PierceViewSet.as_view({'get':'get_piece'}))

]