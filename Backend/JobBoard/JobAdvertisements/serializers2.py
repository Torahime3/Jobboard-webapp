from rest_framework import serializers

# Serializer for JobAdvertisements
# To serialize JobAdvertisements data in JSON
# Attributes:
#   id: Integer -> id of the JobAdvertisements
#   title: String -> title of the JobAdvertisements
#   location : String -> location of the JobAdvertisements
#   contract_type : String -> contract_type of the JobAdvertisements
#   id_company : String -> id_company of the JobAdvertisements
#   Except certain fields : description, date_of_jobadvertisements, id_people -> not needed to return compact Json
class DataSerializerCompact(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    location = serializers.CharField()
    contract_type = serializers.CharField()
    id_company = serializers.CharField()
