from datetime import datetime
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobApplications.models import JobApplications
from .serializers import DataSerializer
from JobAdvertisements.models import JobAdvertisements
from Peoples.models import Peoples
from Login.models import Login
from Companies.models import Companies


@api_view(["GET"])
def get_all_applications(request):
    applications = JobApplications.objects.all()
    serializer = DataSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_application_by_id(request, id):
    jobA = JobApplications.objects.get(pk=id)
    serializer = DataSerializer(jobA, many=False)
    return Response(serializer.data)


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


@api_view(["POST"])
def create(request):
    if request.method == "POST":
        data = request.data
        id_advertisement = data["id_advertisement"]
        id_people = data["id_people"]
        try:
            objet = JobApplications.objects.get(
                id_advertisement=id_advertisement, id_people=id_people
            )
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
                    return Response({"message": "error1"})
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error2"})
