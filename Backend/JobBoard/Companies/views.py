from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    data_list = [
        {
            'name': 'Vitor',
            'location': 'Finland',
            'is_active': True,
            'count': 28
        },
    ]

    return JsonResponse(data_list)
