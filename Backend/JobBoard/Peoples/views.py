from rest_framework.response import Response
from rest_framework.decorators import api_view
from Peoples.models import Peoples
from Peoples.serializers import DataSerializer

@api_view(['GET'])
def get_peoples(request):
    peoples = Peoples.objects.all()
    serializer = DataSerializer(peoples, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_people_by_id(request, id):
        people = Peoples.objects.get(pk=id)
        serializer = DataSerializer(people, many=False)
        return Response(serializer.data)