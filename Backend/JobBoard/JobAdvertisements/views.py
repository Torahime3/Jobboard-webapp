from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobAdvertisements.models import JobAdvertisements
from JobAdvertisements.serializers import DataSerializer
from JobAdvertisements.serializers2 import DataSerializerCompact
from Companies.models import Companies
from Login.models import Login
from Peoples.models import Peoples

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
# Function :
#         getAllDatas -> get all jobs
# Returns :
#         return a response in json containing all the rows of the tabl | This function is used for the front
@api_view(['GET'])
def getAllDatas(request):
    advertisements = JobAdvertisements.objects.filter().values('contract_type', 'title', 'id_company', 'location', 'id')
    serializer = DataSerializerCompact(advertisements, many=True)
    for i in range(len(serializer.data)):
        company = Companies.objects.get(pk=serializer.data[i]['id_company'])
        serializer.data[i]['company_name'] = company.name
    return Response(serializer.data)

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         getAll -> get all jobs
# Returns :
#         return a response in json containing all the rows of the table
@api_view(['GET'])
def getAll(request,token):
    try:
        user = Login.objects.get(token=token)
        role = Peoples.objects.get(pk=user.id_people_id)
        if(role.role == 'Admin'):
            advertisements = JobAdvertisements.objects.all()
            serializer = DataSerializer(advertisements, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error"})

# Method "GET"
# Param :
#         request -> HttpRequest, object request form Django
#         id -> id of the job
# Function :
#         get_JobAdvertisementsById -> get a job with an ID
# Returns :
#         return a response in json containing the row of the table
@api_view(['GET'])
def get_JobAdvertisementsById(request, id):
    job = JobAdvertisements.objects.get(pk=id)
    serializer = DataSerializer(job, many=False)
    data = {
        'id': serializer.data['id'],
        'title': serializer.data['title'],
        'job_domain': serializer.data['job_domain'],
        'description': serializer.data['description'],
        'date_of_jobadvertisements': serializer.data['date_of_jobadvertisements'],
        'location': serializer.data['location'],
        'contract_type': serializer.data['contract_type'],
        'duration_week': serializer.data['duration_week'],
        'id_company': serializer.data['id_company'],
        'id_people': serializer.data['id_people'],
    }
    company = Companies.objects.get(pk=serializer.data['id_company'])
    data['company_name'] = company.name
    return Response(data)

# Method "POST"
# Param :
#         request -> HttpRequest, object request form Django
#         token -> Authentication token
# Function :
#         create -> create a job
# Returns :
#         return a response, to know if the request is 'success','error' or 'invalidAccess'
@api_view(['POST'])
def create(request,token):
    if request.method == 'POST':
        try:
            user = Login.objects.get(token=token)
            role = Peoples.objects.get(pk=user.id_people_id)
            if(role.role == 'Admin' or role.role == 'Recruiter'):
                if request.method == "POST":
                    data = request.data
                    title = data["title"]
                    job_domain = data["job_domain"]
                    description = data["description"]
                    date_of_jobadvertisements = datetime.now()
                    location = data["location"]
                    contract_type = data["contract_type"]
                    duration_week = data["duration_week"]
                    id_cmp = data["id_company"]
                    id_ppl = data["id_people"]
                    try:
                        # check if id_company exist
                        if id_cmp != "":
                            cmp = Companies.objects.filter(pk=id_cmp)
                            if not cmp.exists:
                                return Response({"message": "error"})
                        else:
                            return Response({"message": "error"})
                        
                        # check if id_people exist
                        if id_ppl != "":
                            ppl =  Peoples.objects.filter(pk=id_ppl)
                            if not ppl.exists:
                               return Response({"message": "error"})
                        else: 
                            return Response({"message": "error"})
                        
                        if (contract_type.upper() not in ["CDI", "CDD", "STAGE", "ALTERNANCE", "SAISONNIER", "ÉTÉ"]):
                            return Response({"message": "error"})
                        
                        # create job
                        jobA = JobAdvertisements.objects.create(
                        title=title,
                        job_domain=job_domain,
                        description=description,
                        date_of_jobadvertisements=date_of_jobadvertisements,
                        location=location,
                        contract_type=contract_type.upper(),
                        duration_week=duration_week,
                        id_company_id=id_cmp,
                        id_people_id=id_ppl,
                        )
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
#         update -> update a job with an ID
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
                title = data["title"]
                job_domain = data["job_domain"]
                description = data["description"]
                date_of_jobadvertisements = data["date_of_jobadvertisements"]
                location = data["location"]
                contract_type = data["contract_type"]
                duration_week = data["duration_week"]
                id_cmp = data["id_company"]
                id_ppl = data["id_people"]
                try:
                    # update job
                    jobA = JobAdvertisements.objects.filter(pk=id).update(
                    title=title,
                    job_domain=job_domain,
                    description=description,
                    date_of_jobadvertisements=date_of_jobadvertisements,
                    location=location,
                    contract_type=contract_type,
                    duration_week=duration_week,
                    id_company=id_cmp,
                    id_people=id_ppl,
                    )
                    return Response({"message": "success"})
                except:
                    return Response({"message": "error"})
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
#         delete -> delete a job with an ID
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
                    # delete job
                    jobA = JobAdvertisements.objects.filter(pk=id)
                    if(jobA.exists):
                        jobA.delete()
                        return Response({"message": "success"})
                    else:
                        return Response({"message": "error"})
                except:
                    return Response({"message": "error"})
            else:
                return Response({"message": "error"})   
        else:
            return Response({"message": "invalidAccess"})
    except:
        return Response({"message": "error"})