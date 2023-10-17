from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Peoples.models import Peoples
from Companies.models import Companies
from Peoples.serializers import DataSerializer
from Login.models import Login

# Method POST
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         get_peoples -> get all the rows in the table Peoples
# Returns :
#         return a response contains all rows of the table
@api_view(["GET"])
def get_peoples(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            peoples = Peoples.objects.all()
            serializer = DataSerializer(peoples, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'invalidAccess'})
    except:
        return Response({'message': 'error'})


# Method "GET"
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         get_people_by_id -> get all data in a row with a token
# Returns :
#         return a response with all the data from the token
@api_view(["GET"])
def get_people_by_token(request, token):
    try:
        login_to_get = Login.objects.get(token=token)
        people = Peoples.objects.get(pk=login_to_get.id_people.id)
        serializer = DataSerializer(people, many=False)
        data = {
            "id": serializer.data["id"],
            "url_profile_picture": serializer.data["url_profile_picture"],
            "firstname": serializer.data["firstname"],
            "lastname": serializer.data["lastname"],
            "date_of_birth": serializer.data["date_of_birth"],
            "phone_number": serializer.data["phone_number"],
            "email": serializer.data["email"],
            "domain": serializer.data["domain"],
            "role": serializer.data["role"],
            "id_company": serializer.data["id_company"],
        }
        if serializer.data["id_company"] == None:
            data["company_name"] = "null"
        else:
            company = Companies.objects.get(pk=serializer.data["id_company"])
            data["company_name"] = company.name
        data["message"] = "success"
        return Response(data)
    except:
        return Response({"message": "error"})

# Method "POST"
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         create -> create a now row in the table
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["POST"])
def create(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "POST":
                data = request.data
                email = data["email"]
                try:
                    objet = Peoples.objects.get(email=email)
                    return Response({"message": "exist"})
                except Peoples.DoesNotExist:
                    data = request.data
                    firstname = data["firstname"]
                    lastname = data["lastname"]
                    date_of_birth = data["date_of_birth"]
                    phone_number = data["phone_number"]
                    url_profile_picture = "null"
                    email = data["email"]
                    domain = data["domain"]
                    password = data["password"]
                    role = "User"
                    try:
                        people = Peoples.objects.create(
                            firstname=firstname,
                            lastname=lastname,
                            date_of_birth=date_of_birth,
                            phone_number=phone_number,
                            url_profile_picture=url_profile_picture,
                            email=email,
                            domain=domain,
                            role=role,
                        )
                        passW = make_password(password, salt="jobboard", hasher="default")
                        tok = get_random_string(length=50)
                        login = Login.objects.create(
                            username=str(firstname).lower(),
                            password=passW,
                            email=email,
                            token=tok,
                            id_people_id=people.id,
                        )
                        return Response({"message": "success"})
                    except:
                        return Response({'message': 'error'})
            else:
                return Response({'message': 'invalidAccess'})
    except:
        return Response({'message': 'error'})


# Method "POST"
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         update -> update a row in the table with data in the request
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["POST"])
def update(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "POST":
                data = request.data
                id = data["id"]
                firstname = data["firstname"]
                lastname = data["lastname"]
                date_of_birth = data["date_of_birth"]
                phone_number = data["phone_number"]
                url_profile_picture = data["url_profile_picture"]
                email = data["email"]
                domain = data["domain"]
                role = data["role"]
                company = data["id_company"]
                try:
                    people = Peoples.objects.get(pk=id)
                    people.firstname = firstname
                    people.lastname = lastname
                    people.date_of_birth = date_of_birth
                    people.phone_number = phone_number
                    people.url_profile_picture = url_profile_picture
                    people.email = email
                    people.domain = domain
                    people.role = role
                    if not company == "":
                        id_company = data["id_company"]
                        cmp = Companies.objects.get(pk=id_company)
                        people.id_company = cmp
                    people.save()
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
            else:
                return Response({"message": "error"})
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "invalidAccess"})


# Method "POST"
# Param : 
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         delete -> delete a people with an ID
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["POST"])
def delete(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            if request.method == "POST":
                data = request.data
                id = data["id"]
                try:
                    people = Peoples.objects.get(pk=id)
                    people.delete()
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
    except:
        return Response({"message": "invalidAccess"})

@api_view(["POST"])
def download_img(request):
    if request.method == 'POST' and 'image' in request.FILES:
        data = request.data
        id = data["id"]
        name = Peoples.objects.get(pk=id).firstname
        image = request.FILES['image']
        destination = './../../img/'
        nom_fichier = name+'.jpg'
        fs = FileSystemStorage(location=destination)
        fs.save(nom_fichier, image)

        # Répondre avec un message de succès
        return Response({"message":"success","url":destination})

    return Response({"message":"error"})