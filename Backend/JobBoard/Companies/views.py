from rest_framework.response import Response
from rest_framework.decorators import api_view
from Companies.models import Companies

from Companies.serializers import DataSerializer


@api_view(['GET'])
def getData(request):
    person = Companies.objects.all()
    serializer = DataSerializer(person, many=True)
    return Response(serializer.data)
