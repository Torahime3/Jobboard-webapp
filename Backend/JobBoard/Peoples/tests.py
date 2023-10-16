from django.test import TestCase
from .models import Companies
from django.urls import reverse
from .models import Peoples


class TestCreatePeoplePOST(TestCase):
    def createPeople(self):
        Companies.objects.create(name="Test", description="Test", url_website="Test", city= "Test", address="Test", zipcode="98742")
        # recupere la fonction createPeople du fichier peoples.py
        data = {
            "firstname": "Test",
            "lastname": "Test",
            "date_of_birth": "1995-10-11",
            "phone_number": "0606060606",
            "url_profile_picture": "img/pic_tristan.jpg",
            "email": "test.test@gmail.com",
            "domain": "Informaticien",
            "role": "User",
            "id_company": Companies.objects.get(name="Test"),
        }


        # Utilisez reverse pour obtenir l'URL de la vue que vous souhaitez tester
        url = reverse('views.create_people')

        # Effectuez une requête POST en utilisant self.client.post
        response = self.client.post(url, data)

        # Assurez-vous que la réponse HTTP est un code 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Vous pouvez également effectuer des assertions sur la réponse pour vérifier
        # si la fonction a renvoyé les résultats attendus
        self.assertContains(response, "Résultat attendu")

        # Assurez-vous d'importer votre fonction et d'appeler la fonction avec les données
        resultat = createPeople(data)

        # Comparez le résultat de la fonction avec ce que vous attendez dans la réponse

        people_from_db = Peoples.objects.get(firstname="Test")
        self.assertEqual(data['firstname'], people_from_db.firstname)
        self.assertEqual(response.content, resultat.encode())

class TestGetPeopleGET(TestCase):
    def getPeople(self):
        # recupere la fonction getPeople du fichier peoples.py
        nb_people_1 = Peoples.objects.all().count()
        data = Peoples.objects.create(firstname="Test", lastname="Test", date_of_birth="1995-10-11", phone_number="0606060606", url_profile_picture="img/pic_tristan.jpg", email="test@gmail.com", domain="domain", role="User")
        nb_people = Peoples.objects.all().count()
        Peoples.delete(data)

        people_from_db = Peoples.objects.get(firstname="Test")

        self.assertIsNone(people_from_db)
        self.assertEqual(nb_people, nb_people_1)
