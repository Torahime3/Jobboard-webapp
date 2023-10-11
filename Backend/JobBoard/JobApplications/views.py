from rest_framework.response import Response
from rest_framework.decorators import api_view
from JobApplications.models import JobApplications
from JobApplications.serializers import DataSerializer

@api_view(['GET'])
def get_applications(request):
    jobA = JobApplications.objects.all()
    serializer = DataSerializer(jobA, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_application_by_id(request, id):
    jobA = JobApplications.objects.get(pk=id)
    serializer = DataSerializer(jobA, many=False)
    return Response(serializer.data)