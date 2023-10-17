from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    token = serializers.CharField()