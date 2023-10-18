from http.client import HTTPResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Login.models import Login
from Peoples.models import Peoples
from django.contrib.auth.hashers import make_password
from Login.serializers import DataSerializer

@api_view(['POST'])
def checkAdmin(request):
    if request.method == 'POST':
        data = request.data
        token = data['token']
        try:
            user = Login.objects.get(token=token)
            role = Peoples.objects.get(pk=user.id_people_id)
            if(role.role == 'Admin'):
                return Response({'message': 'success'})
            else:
                return Response({'message': 'error'})
        except:
            return Response({'message': 'error'})

@api_view(['POST'])
def checkValidity(request):
    if request.method == 'POST':
        data = request.data
        email = data['email']
        passw = data['password']
        try:
            user = Login.objects.get(email=email, password=make_password(passw, salt="jobboard", hasher='default'))
            return Response({
                'message': 'success',
                'token': user.token
                })
        except:
            return Response({'message': 'error'})

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         getAll -> get all logins
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(['GET'])
def getAll(request, token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "GET":
                login = Login.objects.all()
                serializer = DataSerializer(login, many=True)
                return Response(serializer.data)
            else:
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
#         delete -> delete a people with an ID
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
                    login = Login.objects.get(pk=id)
                    role_login = Peoples.objects.get(pk=login.id_people_id)
                    if role_login.role == 'Admin' or login.token == token:
                        return Response({"message": "invalidAccess"})
                    else:
                        login.delete()
                        return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error"})
    

# Method "PUT"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         update -> update a people with an ID
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["PUT"])
def update(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "PUT":
                data = request.data
                id = data["id"]
                username = data["username"]
                password = data["password"]
                email = data["email"]
                id_people = data["id_people"]
                try:
                    login = Login.objects.get(pk=id)
                    login.username = username
                    if password != login.password:
                        login.password = make_password(password, salt="jobboard", hasher='default')
                    else:
                        login.password = password
                    login.email = email
                    if id_people != "":
                        people = Peoples.objects.filter(pk=id_people)
                        if people.exists:
                            login.id_people_id = id_people
                        else:
                            return Response({"message": "error"})
                    login.save()
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
            else:
                return Response({"message": "error"})
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "invalidAccess"})