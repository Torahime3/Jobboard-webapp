from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobAdvertisements.models import JobAdvertisements
from JobAdvertisements.serializers import DataSerializer

@api_view(['GET'])
def getAllDatas(request):
    advertisements = JobAdvertisements.objects.filter()
    serializer = DataSerializer(advertisements, many=True)
    return Response(serializer.data)
