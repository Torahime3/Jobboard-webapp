from rest_framework import serializers
from JobAdvertisements.models import JobAdvertisements
from Peoples.models import Peoples

class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    date_of_application = serializers.DateField()
    id_advertisement = serializers.CharField()
    id_people = serializers.CharField()
