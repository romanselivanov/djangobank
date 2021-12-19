from rest_framework import serializers

class DnaSerializer(serializers.Serializer):
    dna = serializers.CharField(max_length=3, min_length=3)
