import os, django, subprocess
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
color = '\033[92m'

command = "python manage.py flush"
user_input = "yes"

try:
    # Exécute la commande avec une entrée utilisateur simulée
    completed_process = subprocess.run(
        command,
        input=user_input,  # Encode l'entrée utilisateur en bytes
        shell=True,
        text=True,  # Spécifie que l'entrée et la sortie sont des chaînes de texte
        check=True
    )

    # Affiche la sortie de la commande
    print("Toutes les tables ont été vidées !")
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de la commande : {e}")


#########################
# Populate the database #
#########################
os.environ['DJANGO_SETTINGS_MODULE'] = 'JobBoard.settings'

django.setup()

from django.contrib.auth.models import User
# Créez un super utilisateur
User.objects.create_superuser(
    username='admin',
    email='admin@localhost',
    password='Jobboard2023'
)
print(color + "Superuser created !")

#Insert new rows in the table Companies
from Companies.models import Companies
# New rows :
Companies.objects.create(name="Google", description="Google est une entreprise américaine de services technologiques fondée en 1998 dans la Silicon Valley.", address="8 rue de la Paix", city="Paris", zipcode="75000", url_website="https://www.google.com/") #id = 1
Companies.objects.create(name="Microsoft", description="Microsoft Corporation est une multinationale informatique et micro-informatique américaine.", address="70 avenue du Général Leclerc", city="Toulouse", zipcode="31000", url_website="https://www.microsoft.com/fr-fr") #id = 2
Companies.objects.create(name="Apple", description="Apple est une entreprise multinationale américaine qui conçoit et commercialise des produits électroniques grand public.", address="1 rue de la République", city="Lyon", zipcode="69000", url_website="https://www.apple.com/fr/") #id = 3
Companies.objects.create(name="Amazon", description="Amazon est une entreprise de commerce électronique américaine basée à Seattle.", address="2 rue de la Liberté", city="Marseille", zipcode="13000", url_website="https://www.amazon.fr/") #id = 4
print(color + "Success creating new objects in Companies !")

#Insert new rows in the table Peoples
from Peoples.models import Peoples
# New rows :
Peoples.objects.create(firstname="Tristan", lastname="Malo", date_of_birth="1995-10-11", phone_number="0606060606", url_profile_picture="img/pic_tristan.jpg", email="tristan.malo@gmail.com", domain="Informaticien", role="User") #id = 1
Peoples.objects.create(firstname="Jean", lastname="Dupont", date_of_birth="1999-12-01", phone_number="0605658547", url_profile_picture="img/pic_jean.jpg", email="jean.dupont@gmail.com", domain="Informaticien", role="User") #id = 2
Peoples.objects.create(firstname="Pierre", lastname="Martin", date_of_birth="2000-01-12", phone_number="0605651247", url_profile_picture="img/pic_pierre.jpg", email="pierre.martin@yahoo.fr", domain="Informaticien", role="User") #id = 3
Peoples.objects.create(firstname="Paul", lastname="Durand", date_of_birth="1996-02-20", phone_number="0651214587", url_profile_picture="img/pic_paul.jpg", email="paul.durand@mail.com", domain="Coiffeur", role="User") #id = 4
Peoples.objects.create(firstname="Jacques", lastname="Lefebvre", date_of_birth="1998-03-15", phone_number="0605658547", url_profile_picture="img/pic_jacques.jpg", email="jacques.lebvre@mail.com", domain="Professeur", role="User") #id = 5
Peoples.objects.create(firstname="Marie", lastname="Dubois", date_of_birth="1997-04-25", phone_number="0604187500", url_profile_picture="img/pic_marie.jpg", email="marie.dubois@cloud.com", domain="Infirmière", role="User") #id = 6
Peoples.objects.create(firstname="Julie", lastname="Leroy", date_of_birth="1995-05-30", phone_number="0698745612", url_profile_picture="img/pic_julie.jpg", email="julie.leroy@mail.com", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=1)) #id = 7
Peoples.objects.create(firstname="Sophie", lastname="Moreau", date_of_birth="1994-06-05", phone_number="0605145432", url_profile_picture="img/pic_sophie.jpg", email="sophie.moreau@toulouse.com", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=2)) #id = 8
Peoples.objects.create(firstname="Lucie", lastname="Roux", date_of_birth="1993-07-10", phone_number="0605145432", url_profile_picture="img/pic_lucie.jpg", email="lucie.roux@mail.com", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=3)) #id = 9
Peoples.objects.create(firstname="Emma", lastname="André", date_of_birth="1992-08-15", phone_number="0605145432", url_profile_picture="img/pic_emma.jpg", email="emma.and@mail.fr", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=4)) #id = 10
Peoples.objects.create(firstname="Nathan", lastname="Dulac", date_of_birth="2003-09-30", phone_number="0665773552", url_profile_picture="img/pic_nathan.jpg", email="nathan.dulac@epitech.eu", domain="Developer", role="Admin") #id = 11
Peoples.objects.create(firstname="Ariirau", lastname="FUCKS", date_of_birth="2002-02-07", phone_number="0652369874", url_profile_picture="img/pic_ariirau.jpg", email="ariirau.fucks@epitech.eu", domain="Developer", role="Admin") #id = 11
print(color + "Success creating new objects in Peoples !")

#New rows for JobAdvertisements :
from JobAdvertisements.models import JobAdvertisements
JobAdvertisements.objects.create(title="Développeur Web", job_domain="Informatique", date_of_jobadvertisements="2023-08-11", location="Paris", contract_type="CDI", duration_week="35", id_company=Companies.objects.get(pk=1), id_people=Peoples.objects.get(pk=7), description="Suspendisse arcu enim, molestie eget dictum et, interdum vitae arcu. Nam ultrices, ligula at sodales fringilla, arcu nulla congue leo, bibendum tincidunt metus tortor in felis. Morbi vitae nisi suscipit, feugiat augue ut, molestie felis. Donec eget nunc nunc. Morbi eu magna mattis, elementum elit at, pharetra felis. Duis mollis arcu convallis, vehicula ligula eget, ornare felis. Nam congue ut libero sed pretium. Nam malesuada ante eu enim lacinia, id varius quam blandit. Donec finibus finibus luctus. Suspendisse potenti. Phasellus velit felis, ultricies vulputate placerat a, gravida ut lectus. Fusce aliquam lorem vitae magna facilisis interdum. Integer vel elementum justo, a posuere ante. Donec condimentum risus vitae arcu condimentum, vitae gravida turpis lobortis.Phasellus vitae enim elit. Etiam suscipit, purus eu pharetra vehicula, enim arcu pharetra neque, sit amet tincidunt leo lacus vel metus. Cras ut convallis ex. Sed nec urna eu nunc elementum pretium sed eu dui. Maecenas ac leo consectetur, porta quam tincidunt, porttitor ipsum. Nulla at purus velit. Cras lacinia interdum molestie. Mauris vel lacus suscipit, pretium justo nec, iaculis orci. Donec id sapien tempus, faucibus nulla commodo, consequat dui. Cras semper mattis turpis, nec pretium arcu gravida non.") #id = 1
JobAdvertisements.objects.create(title="Développeur Mobile", job_domain="Informatique", date_of_jobadvertisements="2023-09-20", location="Toulouse", contract_type="CDI", duration_week="50", id_company=Companies.objects.get(pk=2), id_people=Peoples.objects.get(pk=8), description="Suspendisse arcu enim, molestie eget dictum et, interdum vitae arcu. Nam ultrices, ligula at sodales fringilla, arcu nulla congue leo, bibendum tincidunt metus tortor in felis. Morbi vitae nisi suscipit, feugiat augue ut, molestie felis. Donec eget nunc nunc. Morbi eu magna mattis, elementum elit at, pharetra felis. Duis mollis arcu convallis, vehicula ligula eget, ornare felis. Nam congue ut libero sed pretium. Nam malesuada ante eu enim lacinia, id varius quam blandit. Donec finibus finibus luctus. Suspendisse potenti. Phasellus velit felis, ultricies vulputate placerat a, gravida ut lectus. Fusce aliquam lorem vitae magna facilisis interdum. Integer vel elementum justo, a posuere ante. Donec condimentum risus vitae arcu condimentum, vitae gravida turpis lobortis.Phasellus vitae enim elit. Etiam suscipit, purus eu pharetra vehicula, enim arcu pharetra neque, sit amet tincidunt leo lacus vel metus. Cras ut convallis ex. Sed nec urna eu nunc elementum pretium sed eu dui. Maecenas ac leo consectetur, porta quam tincidunt, porttitor ipsum. Nulla at purus velit. Cras lacinia interdum molestie. Mauris vel lacus suscipit, pretium justo nec, iaculis orci. Donec id sapien tempus, faucibus nulla commodo, consequat dui. Cras semper mattis turpis, nec pretium arcu gravida non.") #id = 2
JobAdvertisements.objects.create(title="Développeur Web", job_domain="Informatique", date_of_jobadvertisements="2023-10-15", location="Lyon", contract_type="CDI", duration_week="35", id_company=Companies.objects.get(pk=3), id_people=Peoples.objects.get(pk=9), description = " In et venenatis est, sit amet bibendum tortor. Nullam sodales eu nibh in scelerisque. Duis scelerisque, eros eget placerat vestibulum, nisi diam ultricies sapien, quis imperdiet urna magna feugiat leo. Pellentesque vulputate lectus a porttitor scelerisque. Maecenas faucibus sollicitudin magna, id tempus libero commodo in. Etiam placerat mauris nulla, nec ullamcorper purus mollis in. In venenatis laoreet arcu ac volutpat. Duis sit amet nibh lacus. Maecenas tempus nunc eu faucibus imperdiet. Suspendisse pulvinar mattis pretium. Maecenas sit amet nibh suscipit, molestie ligula a, tristique magna. Nunc vestibulum dapibus erat, ut elementum sem gravida vel. Ut ornare congue elit sed mattis. Vestibulum vel tincidunt turpis. Phasellus et diam vitae turpis vehicula auctor. Nam volutpat massa vel purus placerat malesuada. Fusce blandit tempor ligula, vel faucibus erat mattis ac. Etiam sed arcu eleifend, laoreet ligula vel, accumsan tellus. Vestibulum pharetra tellus ut finibus commodo. Maecenas tincidunt tempor leo, eu tincidunt mi. Praesent tempor scelerisque purus, eu tincidunt sem viverra quis. Nulla aliquam sapien ut maximus vulputate. Vivamus elit mi, faucibus quis condimentum vitae, pharetra ut mi. Mauris ultrices sollicitudin erat vitae sodales. Nunc tincidunt sapien ac felis consectetur condimentum in at est. Suspendisse lectus urna, pellentesque id metus in, lacinia posuere odio. Mauris suscipit sapien et nunc viverra, vel bibendum est dapibus. Nullam congue sapien nec ipsum accumsan tempus. Suspendisse ac tempus tortor. Nunc quis enim et nibh ultricies mollis. Vestibulum interdum molestie lectus tempus luctus. Vestibulum id arcu est. Aenean venenatis magna in nisl hendrerit, nec efficitur augue gravida. Pellentesque pretium porta tortor ut dignissim. Sed nec convallis lectus. Vivamus enim erat, faucibus eu suscipit nec, ullamcorper at felis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc mollis dui quis ante aliquet sagittis. Sed tincidunt tincidunt eros non rutrum. Maecenas ut ipsum iaculis, viverra risus sed, ultrices tortor. ") #id = 3
JobAdvertisements.objects.create(title="Développeur Web", job_domain="Informatique", date_of_jobadvertisements="2023-11-25", location="Marseille", contract_type="CDI", duration_week="35", id_company=Companies.objects.get(pk=4), id_people=Peoples.objects.get(pk=10), description = " In et venenatis est, sit amet bibendum tortor. Nullam sodales eu nibh in scelerisque. Duis scelerisque, eros eget placerat vestibulum, nisi diam ultricies sapien, quis imperdiet urna magna feugiat leo. Pellentesque vulputate lectus a porttitor scelerisque. Maecenas faucibus sollicitudin magna, id tempus libero commodo in. Etiam placerat mauris nulla, nec ullamcorper purus mollis in. In venenatis laoreet arcu ac volutpat. Duis sit amet nibh lacus. Maecenas tempus nunc eu faucibus imperdiet. Suspendisse pulvinar mattis pretium. Maecenas sit amet nibh suscipit, molestie ligula a, tristique magna. Nunc vestibulum dapibus erat, ut elementum sem gravida vel. Ut ornare congue elit sed mattis. Vestibulum vel tincidunt turpis. Phasellus et diam vitae turpis vehicula auctor. Nam volutpat massa vel purus placerat malesuada. Fusce blandit tempor ligula, vel faucibus erat mattis ac. Etiam sed arcu eleifend, laoreet ligula vel, accumsan tellus. Vestibulum pharetra tellus ut finibus commodo. Maecenas tincidunt tempor leo, eu tincidunt mi. Praesent tempor scelerisque purus, eu tincidunt sem viverra quis. Nulla aliquam sapien ut maximus vulputate. Vivamus elit mi, faucibus quis condimentum vitae, pharetra ut mi. Mauris ultrices sollicitudin erat vitae sodales. Nunc tincidunt sapien ac felis consectetur condimentum in at est. Suspendisse lectus urna, pellentesque id metus in, lacinia posuere odio. Mauris suscipit sapien et nunc viverra, vel bibendum est dapibus. Nullam congue sapien nec ipsum accumsan tempus. Suspendisse ac tempus tortor. Nunc quis enim et nibh ultricies mollis. Vestibulum interdum molestie lectus tempus luctus. Vestibulum id arcu est. Aenean venenatis magna in nisl hendrerit, nec efficitur augue gravida. Pellentesque pretium porta tortor ut dignissim. Sed nec convallis lectus. Vivamus enim erat, faucibus eu suscipit nec, ullamcorper at felis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nunc mollis dui quis ante aliquet sagittis. Sed tincidunt tincidunt eros non rutrum. Maecenas ut ipsum iaculis, viverra risus sed, ultrices tortor. ") #id = 4
print(color + "Success creating new objects in JobAdvertisements !")

#New rows for JobApplications :
from JobApplications.models import JobApplications
JobApplications.objects.create(id_people=Peoples.objects.get(pk=1), id_advertisement=JobAdvertisements.objects.get(pk=1), date_of_application="2023-10-11", firstname=Peoples.objects.get(pk=1).firstname, lastname=Peoples.objects.get(pk=1).lastname,email=Peoples.objects.get(pk=1).email, phone_number=Peoples.objects.get(pk=1).phone_number) #id = 1
JobApplications.objects.create(id_people=Peoples.objects.get(pk=1), id_advertisement=JobAdvertisements.objects.get(pk=2), date_of_application="2023-10-11", firstname=Peoples.objects.get(pk=1).firstname, lastname=Peoples.objects.get(pk=1).lastname,email=Peoples.objects.get(pk=1).email, phone_number=Peoples.objects.get(pk=1).phone_number) #id = 2
JobApplications.objects.create(id_people=Peoples.objects.get(pk=1), id_advertisement=JobAdvertisements.objects.get(pk=3), date_of_application="2023-10-11", firstname=Peoples.objects.get(pk=1).firstname, lastname=Peoples.objects.get(pk=1).lastname,email=Peoples.objects.get(pk=1).email, phone_number=Peoples.objects.get(pk=1).phone_number) #id = 3
JobApplications.objects.create(id_people=Peoples.objects.get(pk=2), id_advertisement=JobAdvertisements.objects.get(pk=1), date_of_application="2023-10-12", firstname=Peoples.objects.get(pk=2).firstname, lastname=Peoples.objects.get(pk=2).lastname,email=Peoples.objects.get(pk=2).email, phone_number=Peoples.objects.get(pk=2).phone_number) #id = 4
JobApplications.objects.create(id_people=Peoples.objects.get(pk=3), id_advertisement=JobAdvertisements.objects.get(pk=1), date_of_application="2023-10-13", firstname=Peoples.objects.get(pk=3).firstname, lastname=Peoples.objects.get(pk=3).lastname,email=Peoples.objects.get(pk=3).email, phone_number=Peoples.objects.get(pk=3).phone_number) #id = 5
JobApplications.objects.create(id_people=Peoples.objects.get(pk=3), id_advertisement=JobAdvertisements.objects.get(pk=2), date_of_application="2023-10-13", firstname=Peoples.objects.get(pk=3).firstname, lastname=Peoples.objects.get(pk=3).lastname,email=Peoples.objects.get(pk=3).email, phone_number=Peoples.objects.get(pk=3).phone_number) #id = 6
JobApplications.objects.create(id_people=Peoples.objects.get(pk=4), id_advertisement=JobAdvertisements.objects.get(pk=1), date_of_application="2023-10-14", firstname=Peoples.objects.get(pk=4).firstname, lastname=Peoples.objects.get(pk=4).lastname,email=Peoples.objects.get(pk=4).email, phone_number=Peoples.objects.get(pk=4).phone_number) #id = 7
JobApplications.objects.create(id_people=Peoples.objects.get(pk=4), id_advertisement=JobAdvertisements.objects.get(pk=2), date_of_application="2023-10-14", firstname=Peoples.objects.get(pk=4).firstname, lastname=Peoples.objects.get(pk=4).lastname,email=Peoples.objects.get(pk=4).email, phone_number=Peoples.objects.get(pk=4).phone_number) #id = 8
JobApplications.objects.create(id_people=Peoples.objects.get(pk=4), id_advertisement=JobAdvertisements.objects.get(pk=3), date_of_application="2023-10-14", firstname=Peoples.objects.get(pk=4).firstname, lastname=Peoples.objects.get(pk=4).lastname,email=Peoples.objects.get(pk=4).email, phone_number=Peoples.objects.get(pk=4).phone_number) #id = 9
print(color + "Success creating new objects in JobApplications !")

from Login.models import Login
Login.objects.create(username="tristan", password=make_password("tristan123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=1).email, token=get_random_string(length=50),id_people=Peoples.objects.get(pk=1))
Login.objects.create(username="jean", password=make_password("jean123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=2).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=2))
Login.objects.create(username="pierre", password=make_password("pierre123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=3).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=3))
Login.objects.create(username="paul", password=make_password("paul123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=4).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=4))
Login.objects.create(username="jacqueslef", password=make_password("jacqueslef123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=5).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=5))
Login.objects.create(username="marie", password=make_password("marie123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=6).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=6))
Login.objects.create(username="julie", password=make_password("julie123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=7).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=7))
Login.objects.create(username="sophie", password=make_password("sophie123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=8).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=8))
Login.objects.create(username="lucie", password=make_password("lucie123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=9).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=9))
Login.objects.create(username="emma", password=make_password("emma123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=10).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=10))
Login.objects.create(username="nathan", password=make_password("nathan123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=11).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=11))
Login.objects.create(username="ariirau", password=make_password("ariirau123", salt="jobboard", hasher="default"), email=Peoples.objetcs.get(pk=12).email, token=get_random_string(length=50), id_people=Peoples.objects.get(pk=12))
print(color + "Success creating new objects in Login !")
