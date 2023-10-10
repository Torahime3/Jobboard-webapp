from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    data_list = {
            'name': 'Vitor',
            'location': 'Finland',
            'is_active': True,
            'count': 28
        }

    return JsonResponse(data_list)
