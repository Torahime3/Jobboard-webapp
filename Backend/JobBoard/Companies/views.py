from django.shortcuts import render
from django.http import JsonResponse

def index (request):
    data = {
        'name': 'Name',
        'location': 'Location',
        'is_active': True,
        'count': 50
    }
    return JsonResponse(data)