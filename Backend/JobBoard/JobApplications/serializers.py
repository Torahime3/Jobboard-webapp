from rest_framework import serializers

# Serializer for JobApplications
# To serialize all JobApplications data (rows) in JSON
# Attributes:
#   id: Integer -> id of the JobApplications
#   firstname: String -> firstname of the JobApplications
#   lastname: String -> lastname of the JobApplications
#   email: String -> email of the JobApplications
#   phone_number: String -> phone_number of the JobApplications
#   date_of_application: Date -> date_of_application of the JobApplications
#   id_advertisement: String -> id_advertisement of the JobApplications
#   id_people: String -> id_people of the JobApplications
class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    firstname = serializers.CharField()
    lastname = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.CharField()
    date_of_application = serializers.DateField()
    id_advertisement = serializers.CharField()
    id_people = serializers.CharField()
