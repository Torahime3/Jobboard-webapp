from rest_framework import serializers


class DataSerializer(serializers.Serializer):
    types = serializers.CharField()

    title = serializers.CharField()
    job_domain = serializers.CharField()
    description = serializers.CharField()
    date_of_jobadvertisements = serializers.DateField()
    location = serializers.CharField()
    contract_type = serializers.CharField()
    duration_week = serializers.CharField()
    id_company = serializers.CharField()
    id_people = serializers.CharField()