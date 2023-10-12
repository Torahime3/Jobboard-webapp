from django.test import TestCase
from .models import Login
from django.contrib.auth.hashers import check_password, make_password

class TestCreationUtilisateur(TestCase):

    def test_creation_utilisateur(self):
        # Crée un nouvel utilisateur avec un mot de passe non haché
        username = "nouvel_utilisateur"
        raw_password = "motdepasse123"
        email = "email.email@mail.com"

        hashed_password = make_password(raw_password)
        user = Login.objects.create(username=username, password=hashed_password, email=email)

        # Récupère l'utilisateur de la base de données
        user_from_db = Login.objects.get(username=username)

        # Vérifie si le mot de passe est correctement haché
        is_password_valid = check_password(raw_password, user_from_db.password)

        # Vérifie si l'utilisateur a été créé correctement
        self.assertEqual(username, user_from_db.username)
        self.assertTrue(is_password_valid)
