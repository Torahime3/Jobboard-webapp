from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
def getData(request):
    person = {'name': 'John', 'age': 30}
    return Response(person)


