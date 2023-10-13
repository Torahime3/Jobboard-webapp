from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Login.models import Login
from Login.serializers import DataSerializer
from django.contrib.auth.hashers import make_password


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