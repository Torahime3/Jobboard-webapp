from rest_framework import serializers


class DataSerializer(serializers.Serializer):

    title = serializers.CharField()
    location = serializers.CharField()
    contract_type = serializers.CharField()
    id_company = serializers.CharField()


