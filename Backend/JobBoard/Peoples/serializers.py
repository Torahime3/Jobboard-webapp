from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    url_profile_picture = serializers.CharField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    date_of_birth = serializers.DateField()
    phone_number = serializers.CharField()
    email = serializers.CharField()
    domain = serializers.CharField()
    role = serializers.CharField()
    id_company = serializers.CharField()

