from django.test import TestCase
from .models import Login
from Peoples.models import Peoples
from django.contrib.auth.hashers import check_password, make_password

# Function to test the creation of a user
# Check if the user is created in the database
# Check if the password is hashed
class TestCreationUtilisateur(TestCase):

    def test_creation_utilisateur(self):
        Peoples.objects.create(firstname="Tristan", lastname="Malo", date_of_birth="1995-10-11", phone_number="0606060606", url_profile_picture="img/pic_tristan.jpg", email="tristan.malo@gmail.com", domain="Informaticien", role="User") #id = 1
        username = "nouvel_utilisateur"
        raw_password = "motdepasse123"
        email = "email.email@mail.com"
        token = "azer1234"
        id_people = Peoples.objects.get(pk=1)

        hashed_password = make_password(raw_password)
        user = Login.objects.create(username=username, password=hashed_password, email=email, token=token, id_people=id_people)


        user_from_db = Login.objects.get(username=username)
        is_password_valid = check_password(raw_password, user_from_db.password)

        self.assertEqual(username, user_from_db.username)
        self.assertTrue(is_password_valid)