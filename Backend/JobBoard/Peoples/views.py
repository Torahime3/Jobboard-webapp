from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Peoples.models import Peoples
from Companies.models import Companies
from Peoples.serializers import DataSerializer
from Login.models import Login

@api_view(['GET'])
def get_peoples(request):
    peoples = Peoples.objects.all()
    serializer = DataSerializer(peoples, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_people_by_token(request, token):
    try:
        login_to_get = Login.objects.get(token=token)
        people = Peoples.objects.get(pk=login_to_get.id_people.id)
        serializer = DataSerializer(people, many=False)
        data = {
            'id': serializer.data['id'],
            'url_profile_picture': serializer.data['url_profile_picture'],
            'firstname': serializer.data['firstname'],
            'lastname': serializer.data['lastname'],
            'date_of_birth': serializer.data['date_of_birth'],
            'phone_number': serializer.data['phone_number'],
            'email': serializer.data['email'],
            'domain': serializer.data['domain'],
            'role': serializer.data['role'],
            'id_company': serializer.data['id_company'],
        }
        if(serializer.data['id_company'] == None):
            data['company_name'] = "null"
        else:
            company = Companies.objects.get(pk=serializer.data['id_company'])
            data['company_name'] = company.name
        data['message'] = 'success'
        return Response(data)
    except:
        return Response({'message': 'error'})

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        data = request.data
        firstname = data['firstname']
        lastname = data['lastname']
        date_of_birth = data['date_of_birth']
        phone_number = data['phone_number']
        url_profile_picture = "null"
        email = data['email']
        domain = data['domain']
        password = data['password']
        role = "User"
        try:
            people = Peoples.objects.create(firstname=firstname, lastname=lastname, date_of_birth=date_of_birth, phone_number=phone_number, url_profile_picture=url_profile_picture, email=email, domain=domain, role=role)
            passW = make_password(password)
            tok = get_random_string(length=50)
            login = Login.objects.create(username=str(firstname).lower(), password = passW, email=email, token=tok, id_people_id=people.id)
            return Response({
                    'message': 'success',
                    'id': people.id
                })
        except:
            return Response({'message': 'error'})