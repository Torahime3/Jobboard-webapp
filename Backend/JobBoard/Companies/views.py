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
    
# # Method "POST"
# # Param : 
# #         request -> HttpRequest, object request form Django
# #         token -> Authentication token
# # Function :
# #         update -> update a company with an ID and some data
# # Returns :
# #         return a response, to know if the request is 'success','error' or 'invalidAccess'
# @api_view(["POST"])
# def update(request,token):

# # Method "POST"
# # Param : 
# #         request -> HttpRequest, object request form Django
# #         token -> Authentication token
# # Function :
# #         create -> create a new company
# # Returns :
# #         return a response, to know if the request is 'success','error' or 'invalidAccess'
# @api_view(["POST"])
# def create(request,token):
    

# Method "DELETE"
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         delete -> delete a company with an ID
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["DELETE"])
def delete(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "DELETE":
                data = request.data
                id = data["id"]
                try:
                    company = Companies.objects.get(pk=id)
                    company.delete()
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error"})