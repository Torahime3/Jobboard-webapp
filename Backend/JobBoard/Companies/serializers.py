from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    zipcode = serializers.CharField(max_length=5)
    url_website = serializers.CharField(max_length=255)
