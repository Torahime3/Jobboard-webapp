from rest_framework import serializers

# Serializer for Login
# To serialize all Login data (rows) in JSON
# Attributes:
#   id: Integer -> id of the Login
#   username: String -> username of the Login
#   password: String -> password of the Login
#   email: String -> email of the Login
#   token: String -> token of the Login
#   id_people: String -> id_people of the Login
class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()
    token = serializers.CharField()
    id_people = serializers.CharField()