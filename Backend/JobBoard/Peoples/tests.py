from django.test import TestCase
from .models import Companies
from django.urls import reverse
from .models import Peoples

# Function test 
# Test to create a People before update.
# Now when we created a People we need a password to associate it with a Login
class TestCreatePeoplePOST(TestCase):
    def createPeople(self):
        Companies.objects.create(name="Test", description="Test", url_website="Test", city= "Test", address="Test", zipcode="98742")
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


        url = reverse('views.create_people')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Résultat attendu")

        resultat = self.createPeople(data)

        people_from_db = Peoples.objects.get(firstname="Test")
        self.assertEqual(data['firstname'], people_from_db.firstname)
        self.assertEqual(response.content, resultat.encode())

# Function test
# Test to delete a People 
class TestGetPeopleGET(TestCase):
    def getPeople(self):

        nb_people_1 = Peoples.objects.all().count()
        data = Peoples.objects.create(firstname="Test", lastname="Test", date_of_birth="1995-10-11", phone_number="0606060606", url_profile_picture="img/pic_tristan.jpg", email="test@gmail.com", domain="domain", role="User")
        nb_people = Peoples.objects.all().count()
        Peoples.delete(data)

        people_from_db = Peoples.objects.get(firstname="Test")

        self.assertIsNone(people_from_db)
        self.assertEqual(nb_people, nb_people_1)
