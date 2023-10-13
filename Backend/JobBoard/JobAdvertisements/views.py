from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobAdvertisements.models import JobAdvertisements
from JobAdvertisements.serializers import DataSerializer

@api_view(['GET'])
def getAllDatas(request):
    advertisements = JobAdvertisements.objects.filter().values('contract_type','title','id_company','location')
    serializer = DataSerializer(advertisements, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_JobAdvertisementsById(request, id):
    person = JobAdvertisements.objects.get(pk=id)
    serializer = DataSerializer(person, many=False)
    return Response(serializer.data)

