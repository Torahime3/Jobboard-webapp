from rest_framework.response import Response
from rest_framework.decorators import api_view
from Companies.models import Companies
from Companies.serializers import DataSerializer
from Login.models import Login
from Peoples.models import Peoples


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

@api_view(['GET'])
def getCompanyWithToken(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            company = Companies.objects.all()
            serializer = DataSerializer(company, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'invalidAccess'})
    except:
        return Response({'message': 'error'})