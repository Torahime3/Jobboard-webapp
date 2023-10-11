from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    date_of_application = serializers.DateField()
    id_advertisement = serializers.IntegerField()
    id_people = serializers.IntegerField()

