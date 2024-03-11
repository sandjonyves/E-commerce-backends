
# from django.test import TestCase
# from.models import *
# from.views import cathegorieViewSet
# from rest_framework.test import APIRequestFactory, force_authenticate
# from rest_framework import status

# class CathegorieViewSetTest(TestCase):
#     def setUp(self):
        
#         self.factory = APIRequestFactory()
#         # self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.marque = Marque.objects.create(name='toyota')
#         self.modele = Modele.objects.create(name='1',id_marque = self.marque)
#         self.cathegorie1 = Cathegorie.objects.create(name="voiture", id_modele=self.modele)
#         self.cathegorie2 = Cathegorie.objects.create(name="moto", id_modele=self.modele)

#     def test_get_cathegorie(self):
#         request = self.factory.get('/cathegorie/1/')
#         # force_authenticate(request, user=self.client.user)
#         view = cathegorieViewSet.as_view()
#         response = view(request, pk=1)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, [
#             {'id': self.cathegorie1.id, 'name': 'voiture', 'id_modele': 1}
#         ])