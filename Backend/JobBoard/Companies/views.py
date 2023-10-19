from rest_framework.response import Response
from rest_framework.decorators import api_view
from Companies.models import Companies
from Companies.serializers import DataSerializer
from Login.models import Login
from Peoples.models import Peoples

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         getCompanyById -> get a company by id
# Returns :
#         return a company with the ID given in argument
@api_view(['GET'])
def getCompanyById(request, token):
    try:
        # check if the user sending the request is an admin
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            data = request.data
            id = data["id"]
            company = Companies.objects.get(pk=id)
            serializer = DataSerializer(company, many=False)
            return Response(serializer.data)
        else:
            return Response({"message":"invalidAccess"})
    except:
        return Response({"message":"error"})

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         getAll -> get all companies
# Returns :
#         return all companies
@api_view(['GET'])
def getAll(request,token):
    try:
        # check if the user sending the request is an admin
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
    
# Method "PUT"
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         update -> update a company with an ID and some data
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["PUT"])
def update(request,token):
    try:
        # check if the user sending the request is an admin
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "PUT":
                data = request.data
                id = data["id"]
                name = data["name"]
                description = data["description"]
                address = data["address"]
                city = data["city"]
                zipcode = data["zipcode"]
                url_website = data["url_website"]
                try:
                    company = Companies.objects.get(pk=id)
                    company.name = name
                    company.description = description
                    company.address = address
                    company.city = city
                    company.zipcode = zipcode
                    company.url_website = url_website
                    company.save()
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error"})

# Method "POST"
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         create -> create a new company
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["POST"])
def create(request,token):
    try:
        # check if the user sending the request is an admin
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "POST":
                data = request.data
                name = data["name"]
                description = data["description"]
                address = data["address"]
                city = data["city"]
                zipcode = data["zipcode"]
                url_website = data["url_website"]
                try:
                    company = Companies.objects.create(name=name, description=description, address=address, city=city, zipcode=zipcode, url_website=url_website)
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error"})

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
        # check if the user sending the request is an admin
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