from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobApplications.models import JobApplications
from .serializers import DataSerializer
from JobAdvertisements.models import JobAdvertisements
from Peoples.models import Peoples
from Login.models import Login
from Companies.models import Companies
from JobAdvertisements.serializers2 import DataSerializerCompact

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
# Function :
#         get_all_applications -> get all JobApplications
# Returns :
#         return all JobApplications
@api_view(["GET"])
def get_all_applications(request):
    applications = JobApplications.objects.all()
    serializer = DataSerializer(applications, many=True)
    return Response(serializer.data)

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         id -> id of JobApplication
# Function :
#         get_application_by_id -> get a JobApplication by id
# Returns :
#         return a JobApplication with the ID given in argument
@api_view(["GET"])
def get_application_by_id(request, id):
    jobA = JobApplications.objects.get(pk=id)
    serializer = DataSerializer(jobA, many=False)
    return Response(serializer.data)

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         get_application_by_id_company -> get a JobApplications by id_company
# Returns :
#         return a JobApplication with the ID of the company given in argument 
@api_view(["GET"])
def get_application_by_id_company(request,token):
    try:
        user = Login.objects.get(token=token)
        people = Peoples.objects.get(pk=user.id_people_id)
        if(people.role == 'Recruiter' or people.role == 'Admin') and request.method == "GET":
            jobAdv = JobAdvertisements.objects.filter(id_company_id=people.id_company_id)
            serializer = DataSerializerCompact(jobAdv, many=True)
            i = 0
            for job in jobAdv:
                jobA = JobApplications.objects.filter(id_advertisement_id=job.id)
                peoples = []
                for application in jobA:
                    serialize = {
                        "firstname": application.firstname,
                        "lastname": application.lastname,
                        "email": application.email,
                        "phone_number": application.phone_number,
                    }
                    peoples.append(serialize)
                serializer.data[i]['peoples'] = peoples
                i += 1
            return Response(serializer.data)
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error"})

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         get_application_by_token -> get a JobApplications by token
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["GET"])
def get_application_by_token(request, token):
    login = Login.objects.get(token=token)
    jobA = JobApplications.objects.filter(id_people=login.id_people)
    serializer = DataSerializer(jobA, many=True)
    i = 0

    for application in jobA:
        idjob = jobA[i].id_advertisement_id
        job_to_add = JobAdvertisements.objects.get(pk=idjob)
        serializer.data[i]["jobA_title"] = job_to_add.title
        serializer.data[i]["jobA_domain"] = job_to_add.job_domain
        serializer.data[i]["jobA_description"] = job_to_add.description
        serializer.data[i]["jobA_location"] = job_to_add.location
        serializer.data[i]["jobA_contract_type"] = job_to_add.contract_type
        serializer.data[i]["jobA_duration_week"] = job_to_add.duration_week
        company_name = Companies.objects.get(pk=job_to_add.id_company_id)
        serializer.data[i]["company_name"] = company_name.name
        i += 1
    return Response(serializer.data)


# Method "POST"
# Param :
#         request -> HttpRequest, object request form Django
# Function :
#         create -> create a JobApplications
# Returns :
#         return a response, to know if the request is 'success','error' or 'exist'
@api_view(["POST"])
def create(request):
    if request.method == "POST":
        data = request.data
        id_advertisement = data["id_advertisement"]
        id_people = data["id_people"]
        data = request.data
        firstname = data["firstname"]
        lastname = data["lastname"]
        email = data["email"]
        phone_number = data["phone_number"]
        date_of_application = datetime.now()
        if id_people == "":
            adv = JobAdvertisements.objects.get(pk=id_advertisement)
            ppl = Peoples.objects.get(pk=0)
            jobA = JobApplications.objects.create(
            firstname=firstname,
            lastname=lastname,
            email=email,
            phone_number=phone_number,
            id_advertisement=adv,
            id_people=ppl,
            date_of_application=date_of_application,
            )
            return Response({"message": "success"})
        else:
            try:
                objet = JobApplications.objects.get(id_advertisement=id_advertisement, id_people=id_people)
                return Response({"message": "exist"})

            except JobApplications.DoesNotExist:
                data = request.data
                firstname = data["firstname"]
                lastname = data["lastname"]
                email = data["email"]
                phone_number = data["phone_number"]
                date_of_application = datetime.now()
                try:
                    adv = JobAdvertisements.objects.get(pk=id_advertisement)
                    people = Peoples.objects.get(pk=id_people)
                    jobA = JobApplications.objects.create(
                        firstname=firstname,
                        lastname=lastname,
                        email=email,
                        phone_number=phone_number,
                        id_advertisement=adv,
                        id_people=people,
                        date_of_application=date_of_application,
                    )
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})

            except JobApplications.MultipleObjectsReturned:
                return Response({"message": "exist"})
    
# Method "PUT"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         update -> update a JobApplications
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(["PUT"])
def update(request, token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin') and request.method == "PUT":
                data = request.data
                id = data["id"]
                firstname = data["firstname"]
                lastname = data["lastname"]
                email = data["email"]
                phone_number = data["phone_number"]
                date_of_application = data["date_of_application"]
                id_people = data["id_people"]
                id_adv = data["id_advertisement"]
                try:
                    jobA = JobApplications.objects.get(pk=id)
                    jobA.firstname = firstname
                    jobA.lastname = lastname
                    jobA.email = email
                    jobA.phone_number = phone_number
                    jobA.date_of_application = date_of_application
                    jobA.id_people_id = id_people
                    jobA.id_advertisement_id = id_adv
                    jobA.save()

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
#         delete -> delete a JobApplications
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
                    jobA = JobApplications.objects.get(pk=id)
                    jobA.delete()
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
    except:
        return Response({"message": "invalidAccess"})
