import os, django

os.environ['DJANGO_SETTINGS_MODULE'] = 'JobBoard.settings'

django.setup()

#Insert new rows in the table Companies
from Companies.models import Companies
# New rows :
Companies.objects.create(name="Google", description="Google est une entreprise américaine de services technologiques fondée en 1998 dans la Silicon Valley.", address="8 rue de la Paix", city="Paris", zipcode="75000", url_website="https://www.google.com/") #id = 3
Companies.objects.create(name="Microsoft", description="Microsoft Corporation est une multinationale informatique et micro-informatique américaine.", address="70 avenue du Général Leclerc", city="Toulouse", zipcode="31000", url_website="https://www.microsoft.com/fr-fr") #id = 4
Companies.objects.create(name="Apple", description="Apple est une entreprise multinationale américaine qui conçoit et commercialise des produits électroniques grand public.", address="1 rue de la République", city="Lyon", zipcode="69000", url_website="https://www.apple.com/fr/") #id = 5
Companies.objects.create(name="Amazon", description="Amazon est une entreprise de commerce électronique américaine basée à Seattle.", address="2 rue de la Liberté", city="Marseille", zipcode="13000", url_website="https://www.amazon.fr/") #id = 6

#Insert new rows in the table Peoples
from Peoples.models import Peoples
# New rows :
Peoples.objects.create(firstname="Tristan", lastname="Malo", date_of_birth="1960-10-11", phone_number="0606060606", url_profile_picture="img/pic_tristan.jpg", email="tristan.malo@gmail.com", domain="Agriculteur", role="User") #id = 5
Peoples.objects.create(firstname="Jean", lastname="Dupont", date_of_birth="1999-12-01", phone_number="0605658547", url_profile_picture="img/pic_jean.jpg", email="jean.dupont@gmail.com", domain="Informaticien", role="User") #id = 6
Peoples.objects.create(firstname="Pierre", lastname="Martin", date_of_birth="2000-01-12", phone_number="0605651247", url_profile_picture="img/pic_pierre.jpg", email="pierre.martin@yahoo.fr", domain="Informaticien", role="User") #id = 7
Peoples.objects.create(firstname="Paul", lastname="Durand", date_of_birth="1996-02-20", phone_number="0651214587", url_profile_picture="img/pic_paul.jpg", email="paul.durand@mail.com", domain="Coiffeur", role="User") #id = 8
Peoples.objects.create(firstname="Jacques", lastname="Lefebvre", date_of_birth="1998-03-15", phone_number="0605658547", url_profile_picture="img/pic_jacques.jpg", email="jacques.lebvre@mail.com", domain="Professeur", role="User") #id = 9
Peoples.objects.create(firstname="Marie", lastname="Dubois", date_of_birth="1997-04-25", phone_number="0604187500", url_profile_picture="img/pic_marie.jpg", email="marie.dubois@cloud.com", domain="Infirmière", role="User") #id = 10
Peoples.objects.create(firstname="Julie", lastname="Leroy", date_of_birth="1995-05-30", phone_number="0698745612", url_profile_picture="img/pic_julie.jpg", email="julie.leroy@mail.com", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=3)) #id = 11
Peoples.objects.create(firstname="Sophie", lastname="Moreau", date_of_birth="1994-06-05", phone_number="0605145432", url_profile_picture="img/pic_sophie.jpg", email="sophie.moreau@toulouse.com", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=4)) #id = 12
Peoples.objects.create(firstname="Lucie", lastname="Roux", date_of_birth="1993-07-10", phone_number="0605145432", url_profile_picture="img/pic_lucie.jpg", email="lucie.roux@mail.com", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=5)) #id = 13
Peoples.objects.create(firstname="Emma", lastname="André", date_of_birth="1992-08-15", phone_number="0605145432", url_profile_picture="img/pic_emma.jpg", email="emma.and@mail.fr", domain="RH", role="Recruiter", id_company=Companies.objects.get(pk=6)) #id = 14

#New rows for JobAdvertisements :
from JobAdvertisements.models import JobAdvertisements
JobAdvertisements.objects.create(title="Développeur Web", job_domain="Informatique", description="Développeur Web", date_of_jobadvertisements="2023-08-11", location="Paris", contract_type="CDI", duration_week="35", id_company=Companies.objects.get(pk=3), id_people=Peoples.objects.get(pk=11))
JobAdvertisements.objects.create(title="Développeur Mobile", job_domain="Informatique", description="Développeur Mobile", date_of_jobadvertisements="2023-09-20", location="Toulouse", contract_type="CDI", duration_week="50", id_company=Companies.objects.get(pk=4), id_people=Peoples.objects.get(pk=12))
JobAdvertisements.objects.create(title="Développeur Web", job_domain="Informatique", description="Développeur Web", date_of_jobadvertisements="2023-10-15", location="Lyon", contract_type="CDI", duration_week="35", id_company=Companies.objects.get(pk=5), id_people=Peoples.objects.get(pk=13))
JobAdvertisements.objects.create(title="Développeur Web", job_domain="Informatique", description="Développeur Web", date_of_jobadvertisements="2023-11-25", location="Marseille", contract_type="CDI", duration_week="35", id_company=Companies.objects.get(pk=6), id_people=Peoples.objects.get(pk=14))