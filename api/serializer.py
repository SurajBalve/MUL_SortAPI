from rest_framework import serializers

class SortRequestSerializer(serializers.Serializer):
    array = serializers.ListField(
        child = serializers.IntegerField(),
        allow_empty = False)
    algorithm = serializers.ChoiceField(
        choices=['bubble', 'selection', 'insertion', 'merge'],
        default='bubble')
    
class SortResponseSerializer(serializers.Serializer):
    sorted_array = serializers.ListField(
        child=serializers.IntegerField())