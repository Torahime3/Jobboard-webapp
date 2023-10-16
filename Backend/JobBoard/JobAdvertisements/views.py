from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobAdvertisements.models import JobAdvertisements
from JobAdvertisements.serializers import DataSerializer
from JobAdvertisements.serializers2 import DataSerializerCompact
from Companies.models import Companies

@api_view(['GET'])
def getAllDatas(request):

    advertisements = JobAdvertisements.objects.filter().values('contract_type', 'title', 'id_company', 'location', 'id')
    serializer = DataSerializerCompact(advertisements, many=True)
    for i in range(len(serializer.data)):
        company = Companies.objects.get(pk=serializer.data[i]['id_company'])
        serializer.data[i]['company_name'] = company.name
    return Response(serializer.data)

@api_view(['GET'])
def get_JobAdvertisementsById(request, id):
    job = JobAdvertisements.objects.get(pk=id)
    serializer = DataSerializer(job, many=False)
    data = {
        'id': serializer.data['id'],
        'title': serializer.data['title'],
        'job_domain': serializer.data['job_domain'],
        'description': serializer.data['description'],
        'date_of_jobadvertisements': serializer.data['date_of_jobadvertisements'],
        'location': serializer.data['location'],
        'contract_type': serializer.data['contract_type'],
        'duration_week': serializer.data['duration_week'],
        'id_company': serializer.data['id_company'],
        'id_people': serializer.data['id_people'],
    }
    company = Companies.objects.get(pk=serializer.data['id_company'])
    data['company_name'] = company.name
    return Response(data)


