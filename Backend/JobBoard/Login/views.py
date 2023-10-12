from rest_framework.response import Response
from rest_framework.decorators import api_view
from Login.models import Login
from Login.serializers import DataSerializer


@api_view(['POST'])
def checkValidity(request):
    if request.method == 'POST':
        data = request.data
        email = data['email']
        passw = data['password']
        try:
            user = Login.objects.get(email=email, password=passw)
            return Response({'message': 'success'})
        except:
            return Response({'message': 'error'})
