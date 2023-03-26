from rest_framework import serializers
from ..models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.FloatField()
    created_date = serializers.DateTimeField(read_only=True)
    is_active = serializers.BooleanField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', validated_data.name)
        instance.description = validated_data.get('description', validated_data.description)
        instance.price = validated_data.get('price', validated_data.price)
        instance.created_date = validated_data.get('created_date', validated_data.created_date)
        instance.is_active = validated_data.get('is_active', validated_data.is_active)
        instance.save()
        return instance
