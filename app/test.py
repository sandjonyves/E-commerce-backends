from django.test import TestCase
from .models import *
from .serializer import *
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.reverse import reverse
from .views import ReadMarque

class ReadMarqueTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.url = reverse('voiture-list')
        print(self.url)
        model = Voiture.objects.get(id=1)
        # voiture=Voiture()
        # voiture.id_modele = model

        self.voiture = Voiture.objects.create(name ='klkl',id_modele=model)

    def test_get_data(self):
        request = self.factory.get(self.url)
        self.assertEqual(request.status_code,status.HTTP_200_OK)
        # view = ReadMarque.as_view({'get': 'perform_get_data'})
        # response = view(request)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, [{
        #     'id': self.voiture.id,
        #     'name': self.voiture.name,
        #     'id_modele': {
        #         'name': self.voiture.id_modele.name,
        #         'id_marque': {
        #             'name': self.voiture.id_modele.id_marque.name
        #         }
        #     }
        # }])


