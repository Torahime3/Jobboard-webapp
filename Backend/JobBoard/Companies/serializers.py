from rest_framework import serializers

# Serializer for Companies
# To serialize all Companies data (rows) in JSON
# Attributes:
#   id: Integer -> id of the Company
#   name: String -> name of the Company
#   description: String -> description of the Company
#   address: String -> address of the Company
#   city: String -> city of the Company
#   zipcode: String -> zipcode of the Company
#   url_website: String -> url_website of the Company
class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=100)
    zipcode = serializers.CharField(max_length=5)
    url_website = serializers.CharField(max_length=255)
