from rest_framework import serializers


class DataSerializerCompact(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    location = serializers.CharField()
    contract_type = serializers.CharField()
    id_company = serializers.CharField()
