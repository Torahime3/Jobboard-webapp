from rest_framework.response import Response
from rest_framework.decorators import api_view
from Peoples.models import Peoples
from Peoples.serializers import DataSerializer
from Login.models import Login

@api_view(['GET'])
def get_peoples(request):
    peoples = Peoples.objects.all()
    serializer = DataSerializer(peoples, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_people_by_token(request, token):
        login_to_get = Login.objects.get(token=token)
        people = Peoples.objects.get(pk=login_to_get.id_people.id)
        serializer = DataSerializer(people, many=False)
        return Response(serializer.data)

@api_view(['POST'])
def create_people(request):
    if request.method == 'POST':
        data = request.data
        firstname = data['firstname']
        lastname = data['lastname']
        date_of_birth = data['date_of_birth']
        phone_number = data['phone_number']
        url_profile_picture = data['url_profile_picture']
        email = data['email']
        domain = data['domain']
        role = data['role']
        people = Peoples.objects.create(firstname=firstname, lastname=lastname, date_of_birth=date_of_birth, phone_number=phone_number, url_profile_picture=url_profile_picture, email=email, domain=domain, role=role)
        serializer = DataSerializer(people, many=False)
        return Response(serializer.data)