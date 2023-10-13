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
    person = JobAdvertisements.objects.get(pk=id)
    serializer = DataSerializer(person, many=False)
    return Response(serializer.data)

