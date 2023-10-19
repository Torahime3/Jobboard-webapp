from rest_framework import serializers

# Serializer for JobAdvertisements
# To serialize all JobAdvertisements data (rows) in JSON
# Attributes:
#   id: Integer -> id of the JobAdvertisements
#   title: String -> title of the JobAdvertisements
#   job_domain : String -> job_domain of the JobAdvertisements
#   description : String -> description of the JobAdvertisements
#   date_of_jobadvertisements : Date -> date_of_jobadvertisements of the JobAdvertisements
#   location : String -> location of the JobAdvertisements
#   contract_type : String -> contract_type of the JobAdvertisements
#   id_company : String -> id_company of the JobAdvertisements
#   id_people : String -> id_people of the JobAdvertisements
class DataSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    job_domain = serializers.CharField()
    description = serializers.CharField()
    date_of_jobadvertisements = serializers.DateField()
    location = serializers.CharField()
    contract_type = serializers.CharField()
    duration_week = serializers.CharField()
    id_company = serializers.CharField()
    id_people = serializers.CharField()
