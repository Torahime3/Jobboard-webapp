from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Login.models import Login
from Peoples.models import Peoples
from django.contrib.auth.hashers import make_password

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