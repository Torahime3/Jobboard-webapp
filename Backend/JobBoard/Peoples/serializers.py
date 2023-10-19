from rest_framework import serializers

# Serializer for Peoples
# To serialize all Peoples data (rows) in JSON
# Attributes:
#   id: Integer -> id of the People
#   url_profile_picture: String -> url_profile_picture of the People
#   firstname: String -> firstname of the People
#   lastname: String -> lastname of the People
#   date_of_birth: Date -> date_of_birth of the People
#   phone_number: String -> phone_number of the People
#   email: String -> email of the People
#   domain: String -> domain of the People
#   role: String -> role of the People
#   id_company: String -> id_company of the People
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

