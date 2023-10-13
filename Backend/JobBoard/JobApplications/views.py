from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobApplications.models import JobApplications
from .serializers import DataSerializer
from JobAdvertisements.models import JobAdvertisements
from Peoples.models import Peoples
from Login.models import Login

@api_view(['GET'])
def get_all_applications(request):
    applications = JobApplications.objects.all()
    serializer = DataSerializer(applications, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_application_by_id(request, id):
    jobA = JobApplications.objects.get(pk=id)
    serializer = DataSerializer(jobA, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def get_application_by_token(request, token):
    people = Login.objects.get(token=token)
    jobA = JobApplications.objects.filter(id_people=people.id)
    serializer = DataSerializer(jobA, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    if request.method == 'POST':
        data = request.data
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        phone_number = data['phone_number']
        id_advertisement = data['id_advertisement']
        id_people = data['id_people']
        date_of_application = data['date_of_application']
        try:
            adv = JobAdvertisements.objects.get(pk=id_advertisement)
            people = Peoples.objects.get(pk=id_people)
            jobA = JobApplications.objects.create(firstname=firstname, lastname=lastname, email=email, phone_number=phone_number, id_advertisement=adv, id_people=people, date_of_application=date_of_application)
            return Response({
                    'message': 'success',
                    'id': jobA.id
                })
        except:
            return Response({'message': 'error'})