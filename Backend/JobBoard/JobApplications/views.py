from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobApplications.models import JobApplications
from .serializers import DataSerializer
from django.http import HttpResponse as httpresponse

@api_view(['GET'])
def get_all_applications(request):
    applications = JobApplications.objects.all()
    serializer = DataSerializer(applications, many=True)
    # for i in range(len(serializer.data)):
    #     serializer.data[i]['id_advertisement'] = serializer.data[i]['id_advertisement']['id']
    #     serializer.data[i]['id_people'] = serializer.data[i]['id_people']['id']
    return Response(serializer.data[0])

# @api_view(['GET'])
# def get_application_by_id(request, id):
#     jobA = JobApplications.objects.get(pk=id)
#     serializer = DataSerializer(jobA, many=False)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def create(request):
#     if request.method == 'POST':
#         data = request.data
#         firstname = data['firstname']
#         lastname = data['lastname']
#         email = data['email']
#         phone_number = data['phone_number']
#         id_advertisement_id = data['id_advertisement_id']
#         id_people_id = data['id_people_id']
#         date_of_application = data['date_of_application']
#         try:
#             jobA = JobApplications.objects.create(firstname=firstname, lastname=lastname, email=email, phone_number=phone_number, id_advertisement_id=id_advertisement_id, id_people_id=id_people_id, date_of_application=date_of_application)
#             return Response({
#                     'message': 'success',
#                     'id': jobA.id
#                 })
#         except:
#             return Response({'message': 'error'})