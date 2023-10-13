from rest_framework.response import Response
from rest_framework.decorators import api_view
from Companies.models import Companies
from Companies.serializers import DataSerializer


@api_view(['GET'])
def getData(request):
    companies = Companies.objects.all()
    serializer = DataSerializer(companies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCompanyById(request, id):
    company = Companies.objects.get(pk=id)
    serializer = DataSerializer(company, many=False)
    return Response(serializer.data) 
