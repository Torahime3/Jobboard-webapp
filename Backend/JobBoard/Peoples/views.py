from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Peoples

# Create your views here.
def index(request):
    data = {
            'name': 'Vitor',
            'location': 'Finland',
            'is_active': True,
            'count': 28
    }
    return JsonResponse(data)

def get_peoples(request):
    # Récupérez toutes les entrées de la table 'Peoples'
    peoples = Peoples.objects.all()

    # Créez une liste de dictionnaires pour stocker les données
    peoples_data = []

    # Parcourez chaque entrée et ajoutez-la à la liste
    for person in peoples:
        peoples_data.append({
            'id': person.id,
            'nom': person.firstname,
            'email': person.lastname,
            'date of birth': person.date_of_birth,
            'phone number': person.phone_number,
            'email': person.email,
            'domain': person.domain,
            'role': person.role,
            'id company': person.id_company_id
        })

    # Renvoyez les données au format JSON
    return JsonResponse({'peoples': peoples_data})

def get_people_by_id(request, people_id):
    person = get_object_or_404(Peoples, id=people_id)

    # Créez un dictionnaire pour stocker les données de la personne
    person_data = {
        'id': person.id,
        'nom': person.firstname,
        'email': person.lastname,
        'date of birth': person.date_of_birth,
        'phone number': person.phone_number,
        'email': person.email,
        'domain': person.domain,
        'role': person.role,
        'id company': person.id_company_id
    }
    return JsonResponse(person_data)